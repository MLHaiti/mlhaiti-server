# mlhaiti-server

> Open source platform 

## core functionalities 
  1. Forum 
  2. Member Profile (CV/portfolio)
  3. Content management (Podcast, Articles, Video)
  4. Job board

## Contributing 

### installation
First you need to create a fork of the project, go
to the mlhaiti-server repository page and click on "Fork" at the top right

For the rest, you need the git tool, which can be found in your distro's package 
manager (Linux and macOS) or downloaded

Then use the following commands:
           
                git clone https://github.com/<YOUR_LOGIN>/mlhaiti-server.git
                cd mlhaiti-server
                git remote add upstream https://github.com/mlhaiti/mlhaiti-server.git
                git fetch upstream
             
where <YOUR_LOGIN> must be replaced by your login on Github, in order to download your fork.

If you want to finish installing and then start a local mlhaiti instance, click on the link corresponding to your operating system.

* [Installing on linux](installing_linux.md)
* [Installing on mac os](installing_macos.md)
* [Installing on windows](installing_windows.md)
  
## workflow and practical details 

* Features and bug fixes are done via Pull Requests (PR)
* These PRs are unitary. No PR that corrects several problems or brings several features will be accepted; the rule is: a PR = a feature or a correction
* The prod branch (called master in standard git flow) contains production code exclusively, so don't bother trying to commit to it!
* The main repository branches (master, prod and the release branch) should only contain PR merges, no direct commits

## Quality Assurance 

* Core reviews
* checking that tests corresponding to the functionality or correction are present, consistent and pass
