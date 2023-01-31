## timeslicer
# 
# Two functions to slice time/depth series into random chunks
import random

def int_splits(int_length, train=0.8, test=0.15, val=0.05):
    '''
    Function to split an integer into seperate 
    training, testing and validation sets. 
    
    Integers are commonly length of timesteps, or other
    timeseries.
    
    slice = the integer you want to split up
    train + test + val needs to equal 1 to work!
    
    '''
    _sum = train+test+val 
    
    if type(int_length) != int:
        print('error! slice is not an integer')
    elif train <= 0:
        print('error, bad value for train')
    elif test <= 0:
        print('error, bad value for test')
    elif val <= 0:
        print('error, bad value for val')
    elif _sum != 1:
        print('error error!, please double check your splits')
        print('train+test+val equals ', _sum, 'instead of 1')
    else:    
        n_train = int(train*int_length)
        n_test = int(test*int_length)
        n_val = int(val*int_length)
        # some errors due to rounding 
        _diff = int_length - (n_train + n_test + n_val)
        n_train = int(n_train+_diff)
        
        return n_train, n_test, n_val


def randomizer(num_train: int, num_test: int, num_val: int):
    '''
    create lists of randomly sampled slices from the entire training set
    '''
    # Adding together train, test, and validation set to confirm it matches number of slices
    total = num_train + num_test + num_val
    
    options = random.sample(range(total), k=total)

    train = options[:num_train]
    print('number of training slices:', len(train))
    
    test = options[num_train:num_train + num_test]
    print('number of testing slices:', len(test))
    
    val = options[num_train + num_test:]
    print('number of validation slices:', len(val))
    
    return train, test, val

# end