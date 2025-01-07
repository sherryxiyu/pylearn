# FAST base vm image create steps

[toc]

Resource package for setup vm: \\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windowsbase_setup


## Create VM
### Get a iso file 
Get ISO image from [shared folder][iso image path]

### Create VM 
> [How to create VM through virt-manager][create VM through virt-manager]  
#### Enable Administrator Account
1. Create Windows OS from iso file
2. Press **Ctrl+Shift+F3** after system step into locale setting
3. Ignore *System Preparation Tools* window.
4. Right click *Windows start*, select `Computer Management -> System Tools -> Local Users and 
   Groups -> Users`
5. open **Properties** for Administrator account, then unselect _Account is disabled_ checkbox.

#### Login as Administrator

> Backup file `C:\Windows\System32\oobe\audit.exe` if possible.

1. Create a file with following contents then execute it.
    ```cmd
    CD /D %windir%\System32\oobe
    icacls audit.exe /save auditAcl
    TAKEOWN /F audit.exe
    icacls audit.exe /grant Administrators:F
    DEL audit.exe
    COPY ..\svchost.exe audit.exe
    icacls .\ /restore auditAcl
    DEL auditAcl
    NET USER
    ```
2. Restart system 
    ```cmd
    shutdown -r -t 0
    ```
3. Delete file `C:\Windows\audit.exe` after back to OS.


## System Settings

### OS Version Check

| OS Name       | OS Version       |
| ------------- | ---------------- |
| win10         | Build 19041.208  |
| WinServer2019 | Build 17763.5576 |

### Remove password of Administrator
- 控制面板\用户帐户\用户帐户\管理账户\更改账户

### Change System Language
- According to custom prefer, Change System language at `Time&Language -> Language -> 
  Windows display language`
- In order to application could show Chinese words, set `Administrative language settings > 
  Administrative(table) > Change system locale` to `Chinese(Simplified, China)` and leave `Beta ...` unselect.

### Network Proxy
Setting system network proxy as application will need it.
- Proxy address: *192.168.20.111:3128*

### Setting `Power Plan` to _High Performance_ Mode
Go to `Control Panel\Hardware and Sound\Power Options` in `Control Panel`, setting *Preferred 
plans* to *High performance*.

### Enable/Disable Test Signature Driver
Turn on/off driver signature check.
```shell
bcdedit /set testsigning on  # turn on
bcdedit /set testsigning off  # turn off
```

### Disable System Upgrade
Disable system auto upgrade, use script in [shared folder][disable windows update] 
or [manually][disable windows update link].

### Enable RDP
- Turn on `Remote Desktop` in `Settings -> Remote Desktop`
- Allow blank password to access Desktop.
1. Open `Local Security Policy`
2. Select `Local Policies -> Security Options`
3. Select Policy `Accounts: Limit local account use of blank passwords to console logon only` to 
   **Disable**.

### File Structure
- Create folder `C:\pkg-to-run\fast`
- Add `PYTHONPATH=C:\pkg-to-run\fast` to _User Environment Variables_.

### Disable New Network Discover Prompt
Adding the registry key, `HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Network
\NewNetworkWindowOff`, to prevent prompt "allow PC to be discoverable on this network".

### Making System Crash from the Keyboard Valid
Define which key used to trigger system crash. For details setting refer to
[Forcing a system crash from the keyboard][Forcing a system crash from the keyboard]
Register key path `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\i8042prt\crashdump`.

| key Name  | type      | Data       |
| --------- | --------- | ---------- |
| Dump1Keys | REG_DWORD | 0x00000010 |
| Dump2Key  | REG_DWORD | 0x0000003d |


## Basic Tools

### Install TightVNC service
- Get [TightVNC installer][TightVNC installer]
- Use default setting of installer to install TightVNC.
- Suggest: Open `TightVNC Service Configuration` by clicking `TightVNC` icon `System Tray`, then
  Unselect `Hide desktop wallpaper`.

### Install Python3 and Related Modules

#### Install Python3
- Get [python3.8 installer][python3.8 installer]
- Install with default setting.
- Check Python3 install successful. 
  - Open command prompt and type `py` or `python`

#### Install Modules for Python3

Install packages for automatic test further.
```bash
py -m pip install pyyaml -i https://pypi.mirrors.ustc.edu.cn/simple/
py -m pip install grpcio grpcio-tools -i https://pypi.mirrors.ustc.edu.cn/simple/
py -m pip install pywinauto selenium -i https://pypi.mirrors.ustc.edu.cn/simple/
```
> For internal network, use pip repo `-i http://192.168.20.247:8081/repository/pip/simple/ --trusted-host 192.168.20.247`
> If you can't use pip, then get site-packages.zip from shared directory \\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\Tools--开发者中心 
> and then put it to C:\Users\username\AppData\Local\Programs\Python\Python38\Lib and unzip site-packages.zip

### gRpc Server
For detail operateion, please refer to [How to auto rdp for windows vms][auto rdp vms]
1. Copy "\\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windowsbase_setup\deploy" to 
`C:\pkg-to-run`
2. Put _start up script_ to _user start up_ folder
    - Call `run` by pressing **Win+R**
    - Type `shell:startup` and open, the _user start up_ folder will show.
    - Copy `C:\pkg-to-run\deploy\grpc_server.bat` to _user start up_ folder.
3. Auto login the machine of receiving IP info with non-password.
4. Double click `grpc_server.bat` in _user start up_ folder.
    - Make sure script could run successful
    - Check remote machine have received IP info
    - Check gRpc server could accept request from gRpc client.

> Recommending to delete `C:\pkg-to-run\fast\vm_ip_info.txt` file before shutdown base VM.

> For get VM ip method, could be use [bridge host and windows guest][qemu guest agent] instead.

### gRpc Server - Replacement
It's on plan to replace to install gRpc server as system service through `nssm` tool.

### `windbg` Script
Put enable `windbg` script in base VM, in case VM hang need to debug.
For detail operation, refer to [VM windbg setting][vm windbg]

### Avoiding System BSOD
#### Sysinternal Tools
`sync` tool could flush memory cache content to disk to avoid system BSOD.
1. Downloading `sync` tool from [Microsoft Learn - Sysinternals][sysinternals]
2. Launch first time `sync` and agree the license.
3. Put executable application to `C:\Programs Files\Sync`

### Disable System Recovery
```shell
bcdedit /set recoveryenabled No
```

## Fast Environment

- Install ludashi: "\\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windowsbase_setup\setup.exe"
    1. Get installer from [ludashi installer][ludashi] and execute it.
    2. after install finished, run "硬件评测" for one time to download the evaluate resources.
    3. open "Windows Defender Firewall"->Advanced settings->Outbound Rules->New Rule->choose 
     "Program", next->This program path, browse->add a exe file in folder C:\Program Files (x86)\LuDaShi, next-> input a name
    4. repeat step 2, add all exe file in folder C:\Program Files (x86)\LuDaShi
    5. disable ludashi tools after power on PC: https://jingyan.baidu.
   com/article/d5a880ebdb222152f147ccc6.html

- Install Chrome & 360X WebBrowser:
    1. "\\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windows安装包\ChromeStandaloneSetup64.exe"
    2. "\\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windows安装包\360csex_setup.exe"
    3. Win+R and input "services.msc", STOP all Google-related services and set <Startup Type> to Disable
    4. DELETE "C:\Users\Administrator\AppData\Local\360ChromeX\Chrome\Application\21.0.1200.0\installer" folder

- Install VC Runtime
Get installer from [VC runtime installer][VC Runtime] and execute it. 

# END

[iso image path]: \\vsshare1.vastai.com\ShareFiles\GPU_SW\Shiyang\OS_image\cn_windows_10_business_editions_version_2004_x64_dvd_c59a4f91.iso
[create VM through virt-manager]: http://confluence.vastai.com/pages/viewpage.action?spaceKey=GPUSW&title=How+to+setup+kvm+environment+on+ubuntu+system
[enable Administrator]: https://blog.51cto.com/u_14322706/5621611
[disable windows update]: \\vsshare1.vastai.com\ShareFiles\GPU_SW\Shiyang\OS_image\disable_windows_update
[disable windows update link]: https://www.disktool.cn/content-center/win10-turn-off-automatic-update-method-2111.html
[TightVNC installer]: \\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windowsbase_setup\tightvnc-2.8.81-gpl-setup-64bit.msi
[python3.8 installer]: \\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windowsbase_setup\python-3.8.10-amd64.exe
[auto rdp vms]: http://confluence.vastai.com/display/GPUSW/How+to+auto+rdp+for+windows+vms
[vm windbg]: http://confluence.vastai.com/pages/viewpage.action?pageId=23054482
[sysinternals]: https://learn.microsoft.com/en-us/sysinternals/downloads/sync
[qemu guest agent]: http://confluence.vastai.com/display/GPUSW/How+To+Bridge+Host+and+Windows+Guest
[Forcing a system crash from the keyboard]: https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/forcing-a-system-crash-from-the-keyboard
[VC Runtime]: \\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windowsbase_setup\vc运行时.rar
[ludashi]: \\vsshare1.vastai.com\ShareFiles\GPU_SW\Integration\windowsbase_setup\setup.exe