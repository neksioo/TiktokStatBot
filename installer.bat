@echo off
MODE 80,1
title [TiktokStatBot Installer] - Installing modules: discum
pip install discum
cls
title [TiktokStatBot Installer] - Installing modules: ctypes
pip install ctypes
cls
title [TiktokStatBot Installer] - Installing modules: json
pip install json
cls
title [TiktokStatBot Installer] - Installing modules: string
pip install string
cls
title [TiktokStatBot Installer] - Installing modules: random
pip install random
cls
title [TiktokStatBot Installer] - Installing modules: os
pip install os
cls
title [TiktokStatBot Installer] - Installing modules: datetime
pip install datetime
cls
title [TiktokStatBot Installer] - Installing modules: colorama
pip install colorama
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
