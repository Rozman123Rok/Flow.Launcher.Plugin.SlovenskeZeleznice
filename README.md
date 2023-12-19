# Flow.Launcher.Plugin.SlovenskeZeleznice

This is a FlowLauncher plugin designed to provide train schedule information between the Poljčane and Maribor stations. It displays departure times and estimated arrival times for trains on this route. This plugin was created for my personal use and so this is why it is not added to Flow's Plugin Store.

## Example
![Screenshot](/Images/screenshot.png)


## Usage
This are commands for using this plugin.
| Command | Example | Description |
| -------- | -------- | -------- |
| sz 1  | sz  1 | Provides train schedule information between Poljčane and Maribor stations.   |
| sz 2  | sz  2 | Provides train schedule information between Maribor and Poljčane stations.   |
| sz  | sz  | Provides train schedule information between Maribor and Poljčane stations.   |


## Installation
There are two ways to install plugin for personal use. Because plugin was not added to Flow's Plugin Store it must be installed manualy.

1. Download zip file
- from [GitHub](https://github.com/Rozman123Rok/Flow.Launcher.Plugin.SlovenskeZeleznice) download zip file
- save and unzip in %APPDATA%\Roaming\FlowLauncher\Plugins\
- restart Flow Launcher `restart Flow Launcher`
- you can now use my plugin

2. Install
- clone repository in %APPDATA%\Roaming\FlowLauncher\Plugins\ 
-  move inside plugin folder and install dependencies `pip install -r requirements.txt --target ./lib`
- restart Flow Launcher `restart Flow Launcher`
- you can now use my plugin


### TODO
- [x] Fix date in url
- [x] Add to show trains schedule in other direction (Maribor -> Poljčane)
- [ ] Add possibility to set stations in plugin settings -> would have to edit scraper
- [ ] Add to display delay time in subtext