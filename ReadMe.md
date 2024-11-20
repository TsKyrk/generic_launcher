# Generic_Launcher
This tool aims at remplacing an existing windows executable file by a launcher that will read a configuration file named `generic_launcher_configuration.txt` and execute the containing one-liner command instead of the original executable file that has been overwritten.

# Example 1
If the input one-liner command is `echo This is a standard output&& echo This is a standard error>&2` then the execution of `generic_launcher.exe` will execute the configured command. The message displayed in stdout will be `This is a standard output` and the message displayed in stderr will be `This is a standard error`.

# Example 2
If the input one-liner command is `echo` then the execution of `generic_launcher.exe toto tata -com test` will be equivalent to the command `echo toto tata -com test`. The message displayed will be `toto tata -com test`.

# Build
Run `build.bat`. This will generate the executable file here `dist\generic_launcher.exe`.

# Test
Open the subfolder `dist`.
Run `test_generic_launcher.bat`. This will 
- execute a reference command and save the result in 2 output files. 
- execute `generic_launcher.exe` and save the result in 2 output files.
- compare the output files (stdout vs stdout) and (stderr vs stderr). There should be no difference. 

# Use
Replace the executable file of your choice with `generic_launcher.exe` and in the same folder, add a file `generic_launcher_configuration.txt`. In this configuration file, set the alternative command that should be run instead of the overwritten executable.

# Todo
Nothing.