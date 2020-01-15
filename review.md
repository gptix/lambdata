## Code Review for `lambdata`

### Overall Score: 2

### Review Notes:
It looks like this `lambdata` package meets all the requirements, having two helper functions and having an initial upload to TestPyPi. The only suggestions I have are ones that we've already discussed -- using a stylecheck to adjust some minor style issues, and then re-uploading to TestPyPi so the package can be functional. I might also suggest specifying the `test_size` parameter in the sklearn `train_test_split` functions, rather than the `train_size` to make it easier to have a more even train/val/test percentage splits, and still have easy math. Overall though, I think it's great, and I learned something new from your use of the `train_test_split` function, so thank you!