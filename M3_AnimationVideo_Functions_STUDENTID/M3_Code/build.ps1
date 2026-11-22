# ==============================================================================
# Windows PowerShell Build and Render Script for M3 Animation Video
# Single-Variable Functions & Graphs: f(x) = x^3 - 3x
# Student: Abhinav Singh (ID: E25B070774)
# ==============================================================================

param(
    [string]$Mode = "production"
)

$ErrorActionPreference = "Stop"

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host " M3 Animation Video: Single-Variable Functions & Graphs" -ForegroundColor Cyan
Write-Host " Student: Abhinav Singh | ID: E25B070774" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

# Check Python and FFmpeg
if (-not (Get-Command ffmpeg -ErrorAction SilentlyContinue)) {
    Write-Warning "FFmpeg not found on PATH. Please install via: choco install ffmpeg"
}

$Python = "python"
if (Test-Path ".venv\Scripts\python.exe") {
    $Python = ".venv\Scripts\python.exe"
}

# Run Pytest
Write-Host "`n[*] Running SymPy mathematical verification tests..." -ForegroundColor Yellow
& $Python -m pytest tests/test_math.py -v
if ($LASTEXITCODE -ne 0) {
    Write-Error "Mathematical verification tests failed! Halting build."
    exit 1
}

# Render settings
if ($Mode -eq "preview") {
    Write-Host "`n[*] Rendering in PREVIEW mode (854x480 @ 15 fps)..." -ForegroundColor Green
    $ResFlags = @("-r", "854,480", "--fps", "15")
    $QualityDir = "480p15"
} else {
    Write-Host "`n[*] Rendering in PRODUCTION mode (1920x1080 @ 30 fps)..." -ForegroundColor Green
    $ResFlags = @("-r", "1920,1080", "--fps", "30")
    $QualityDir = "1080p30"
}

$Scenes = @(
    @("scene1_hook.py", "Scene1Hook"),
    @("scene2_concept.py", "Scene2Concept"),
    @("scene3_intuition.py", "Scene3Intuition"),
    @("scene4_worked_example.py", "Scene4WorkedExample"),
    @("scene5_interpretation.py", "Scene5Interpretation"),
    @("scene6_summary.py", "Scene6Summary")
)

foreach ($s in $Scenes) {
    $file = $s[0]
    $cls = $s[1]
    Write-Host "`n>>> Rendering $cls from $file..." -ForegroundColor Cyan
    & $Python -m manim @ResFlags $file $cls
}

# Generate Storyboard PDF
Write-Host "`n[*] Generating Storyboard.pdf..." -ForegroundColor Yellow
& $Python generate_storyboard_pdf.py

# Concatenate scenes
Write-Host "`n[*] Stitching scenes with FFmpeg..." -ForegroundColor Yellow
$ConcatFile = "concat_list.txt"
if (Test-Path $ConcatFile) { Remove-Item $ConcatFile }

foreach ($s in $Scenes) {
    $cls = $s[1]
    $path = "media/videos/$($s[0].Replace('.py',''))/$QualityDir/$cls.mp4"
    "file '$path'" | Out-File -FilePath $ConcatFile -Append -Encoding ascii
}

$OutputFile = "../M3_Video.mp4"
if (Test-Path $OutputFile) { Remove-Item $OutputFile }

ffmpeg -y -f concat -safe 0 -i $ConcatFile -c:v libx264 -pix_fmt yuv420p -c:a aac $OutputFile
Remove-Item $ConcatFile

Write-Host "`n======================================================================" -ForegroundColor Green
Write-Host " BUILD COMPLETE! Final video: $OutputFile" -ForegroundColor Green
Write-Host "======================================================================" -ForegroundColor Green
