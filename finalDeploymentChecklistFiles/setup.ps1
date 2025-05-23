Invoke-WebRequest -UseBasicParsing https://... | Invoke-Expression
$ErrorActionPreference = "Stop"
Write-Host "📦 Installing AIImageTokenSaver..."

$targetDir = "$env:ProgramFiles\AIImageTokenSaver"
$exePath = "$targetDir\AIImageTokenSaver.exe"
$iconPath = "$targetDir\tray_icon.ico"
$shortcutPath = "$env:USERPROFILE\Desktop\AIImageTokenSaver.lnk"

# Create target directory
if (-Not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null
}

# Download EXE and icon
Invoke-WebRequest -Uri "https://github.com/anombyte93/AIImageTokenSaver/releases/latest/download/AIImageTokenSaver.exe" -OutFile $exePath
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/anombyte93/AIImageTokenSaver/main/tray_icon.ico" -OutFile $iconPath

# Create desktop shortcut
$shell = New-Object -ComObject WScript.Shell
$shortcut = $shell.CreateShortcut($shortcutPath)
$shortcut.TargetPath = $exePath
$shortcut.WorkingDirectory = $targetDir
$shortcut.IconLocation = $iconPath
$shortcut.Save()

# Prompt the user with options
Add-Type -AssemblyName PresentationFramework
$response = [System.Windows.MessageBox]::Show(
    "AIImageTokenSaver has been installed.\n\nDo you want to launch the app now?",
    "Installation Complete",
    [System.Windows.MessageBoxButton]::YesNoCancel,
    [System.Windows.MessageBoxImage]::Information
)

switch ($response) {
    "Yes" {
        Start-Process $exePath
    }
    "No" {
        Write-Host "Installation complete. You can run the app later from Desktop or Program Files."
    }
    "Cancel" {
        Write-Host "Cancelled by user."
    }
}

Write-Host "✅ Done!"
