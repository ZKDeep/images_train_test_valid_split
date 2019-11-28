# images_train_test_valid_split
You have single Class wise image Directory for deep learning and want to split it into train, test and validation. You can easily do it with this script.

1. Select the directory in which you have class wise folders that are not split into train test and validation.
2. import the images_train_test_valid_split
3. call the function images_train_test_valid_split and pass two parameters
    a. target_directory
    b. a list describing train test split ratio for instance [0.30, 0.20], first indice is the percentage split from train to test and the        second one is the percentage split for validation.
    
4. All is done and you have Train, test and valid distribution of images from main Dataset.
