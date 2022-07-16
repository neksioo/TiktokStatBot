@echo off
MODE 80,1
title [TiktokStatBot Installer] - Installing modules: discord
pip install discord
cls
title [TiktokStatBot Installer] - Installing modules: requests
pip install requests
cls
title [TiktokStatBot Installer] - Installing modules: time
pip install time
cls
title [TiktokStatBot Installer] - Installing modules: os
pip install os
cls
title [TiktokStatBot Installer] - Installing modules: fake_headers
pip install fake_headers
cls
title [TiktokStatBot Installer] - Modules installed
timeout 2 >nul
title [TiktokStatBot Installer] - Opening config.json file
timeout 2 >nul
start config.json
timeout 2 >nul
title [TiktokStatBot Installer] - Opened config.json file
timeout 2 >nul
title [TiktokStatBot Installer] - Click anything to open main.py
timeout 2 >nul
start main.py
@echo>"launcher.bat"
set file="launcher.bat"
echo @echo off> %file%
echo start main.py>> %file%
del installer.bat
