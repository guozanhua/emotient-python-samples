# Emotient Analytics Python SDK Scripts

These scripts work on top of the Emotient Analytics Python SDK and automate tasks. 

To install the Emotient Analytics Python SDK, see <https://github.com/emotient/emotient-python>.  For information on the Emotient Analytics API, see <https://analytics.emotient.com/apireference/>.


## Running a Script

Run the scripts from the command line. For example:


```
cd your/user/path/emotient-python-samples
python batch-delete.py -k "91se93z0-f73f-498a-b744-8d1e3a061fcf"
```
## Configuration
All scripts require your API key to authenticate with the Emotient Analytics API. Batch-upload.py and batch-download.py also require a directory path. Configure your scripts like so:

```
python batch-download.py -k "91se93z0-f73f-498a-b744-8d1e3a061fcf" -d "my/user/path/videos"
```

Batch-delete.py also accepts the configuration "-y" to bypass the step asking you to confirm the deletion of all videos.


## Scripts
This folder contains the following scripts:

* batch-upload.py: Upload all videos from a specified directory.
* batch-download.py: Download CSV data for all videos to a specified directory. 
* batch-delete.py: Delete all videos from your Emotient Analytics account (careful! this is irreversible).

## Contributing
1. Fork it (<https://github.com/emotient/emotient-python-samples>).
2. Create your script branch with `git checkout -b my-edit`
3. Commit your changes with `git commit -am 'Add some change'`
4. Push to the branch with `git push origin my-edit`
5. Create a new Pull Request.

## Support

For more information, send us an email at <support@emotient.com>.