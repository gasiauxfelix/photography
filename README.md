<img src="https://i.imgur.com/ZG4gSnb.jpeg" alt="demo"/>

# Photography ![OpenCollective](https://opencollective.com/photography/tiers/backer/badge.svg?label=backer&color=brightgreen)
A jekyll website for photographers

## Highlights
1. Easy setup and you get a website of your own for __free__. No web hosting charges too.
2. To add new pictures, you need to just upload them. __No code__ changes required.
3. And, my favorite, you get to see EXIF data like __aperture, shutter speed, iso__ etc. when you click on any image, automagically. Moreover, you can customize this as per your needs.

## Quick Start

**Just follow the below steps and your website would be live in no time:**

1. Fork this repo by hitting the `Fork` button at the top right corner.
2. Enable github pages from the repo settings.
3. Upload your pictures to `images/fulls` and `images/thumbs` directory. _You can do that on github.com itself or you can clone and push the images to your repo._
4. Add your own custom domain in `CNAME` file or just remove the file if you don't own a domain and use the default domain that github provides ([yourusername].github.io/photography).
5. Update `baseurl` field in `_config.yml` file with whatever domain you used in step 4.
6. And that's it, your website is set. To view, go to [photography.rampatra.com](http://photography.rampatra.com) (or whatever you have in the CNAME file) and if you don't have one, you can go to [[yourusername].github.io/photography](http://yourusername.github.io/photography)

And, of course, you don't want my name at the bottom to show up. You can change it in `_config.yml` file as well as a few other settings like your social links, google analytics, etc. Just do not forget to [build the website](#build-the-website) after you make the changes.
 
## ProTips

### Resize Images

For future reference, this single line works pretty well: 
`mogrify -path ./thumbs -resize 512x ./fulls/*` 

### Contact Form
You can make the contact form work without the need of any server-side code. Just follow this [article on github](https://github.com/dwyl/html-form-send-email-via-google-script-without-server) which uses a simple google script to send emails or to upload to a google spreadsheet when someone submits the form.

## Credits
Thanks to [AJ](https://twitter.com/ajlkn) for the website template which I enhanced for [jekyll](http://jekyllrb.com/).

