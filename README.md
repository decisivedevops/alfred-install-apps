# Alfred App Install
Install your downloaded Mac OS Applications right from [Alfred](https://www.alfredapp.com/).

## How to install
Download the [workflow](https://github.com/decisivedevops/alfred-install-apps/blob/main/Installing%20Apps.alfredworkflow). Double click to install directly to Alfred.

## How to use
**Alfred App Install** searches through your `~/Downloads` folder and lists installable Objects like `.zip` or `.dmg` in Alfred. Upon selection, it will automatically install it to your `/Applications/` folder.

The script will run through the supplied paths and list all supported filetypes. It will then install (copy) all `.app`s to your `/Applications/` folder, it will then delete the source.

![](./images/img-1.png)

#### As Keyword:
* Simply type `install` into Alfred
* Select the installable file and install with `Enter`

## Supported Filetypes
App Install will find and install the following files:

* Disk Images `.dmg`:
    - Will automatically mount and unmount the Image, installing all `.app` inside.
* Archives `.zip`:
    - Will extract the zip to a temporary location and install all `.app` inside.

<!-- ROADMAP -->
## Roadmap
https://trello.com/b/sRyBw2X5/alfred-install-apps

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [fgr0/dmginstall](https://github.com/fgr0/dmginstall)
