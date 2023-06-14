![example workflow](https://github.com/limonije/FullStack_CD/actions/workflows/run-tests.yml/badge.svg)

# Report Assignment CD

## CI/CD process
![CI/CD](https://www.cloud4y.ru/upload/medialibrary/6c4/n5sh4bmwki7j7mpveh4zway0e0mmwb5t/CI_CD.png)

### Main Components List

- [x] GitHub
- [x] SSH
- [x] Digital Ocean

In the CI part of the process GitHub is the main component of the solution. The code for the flask app is written in VS Code and then committed to GitHub. The Test is done via a GitHub Action (run-tests.yml) automatically on each new commit. Before the app can be released the tests need to be successfull. In order to release and deploy the app (the CD part of the process) in a secure way SSH keys are set up on the server side (Digital Ocean) and the public key added to the GitHub repository and the private key set in a action secret. The automatic deployment is done in the second part of the GitHub action. The main.py file is placed in the farm directory on the Digital Ocean droplet. Also the app is restarted in order to see the updated version of the app in the browser via the ip-address of the droplet.

### Troubleshooting

## Testing
I needed three unsuccessfull commits to find out how make the GitHub action for testing succesfull. First I needed to add to the requirements.txt the flask version. When I looked for the flask version on the CLI, I noticed also a version for Werkzeug was mentioned, so I included that as well. The workflow was still unsuccesfull and in the report I noticed I made an error in the test_main.py with two same client.get commands. When that was fixed the workflow was successfull! It shows again the importance of testing. 

## SSH Keys
Then it was time to set up the SSH Keys. I entered the built-in console of Digital Ocean and everything seems to go right. When I run the second part of the workflow I got in the report the error message:

`handshake failed: ssh: unable to authenticate, attempted methods [non publickey]`

Since I work on Windows and uses OpenSSH, I found a first solution in updating the sshd_config file. However I still received the same error message. My final solution was to use ed25519 keys and this worked.

## Restarting the app
After the deployment succeeded I wanted to check in the browser if the app also worked, but I received the information from the old main.py from the farm excersize. I realised the command systemctl restart nginx in the workflow was not working. I found some documentation that you had to refer to your app service, so when I changed it in system restart farm, everything worked!

### Conclusion

I now have a better understanding how deployment works and how you can automate the process. Again the importance of testing is clear and it makes sense now why you would like to have testers in your team who can write good testing scripts.