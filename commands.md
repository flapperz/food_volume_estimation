```
$train_df = "G:\My Drive\Senior Project\dataset\form\train_df.csv"
$config = "G:\My Drive\Senior Project\dataset\form\config.json"
$B = 8
$E = 6
$name = "train_testing"
$initial_w = "C:\Source\food_volume_estimation\trained_models/train_testing_weights_epoch_6.h5"

python food_volume_estimation\depth_estimation\monovideo.py --train --train_dataframe $train_df --config $config `
--batch_size $B --training_epochs $E --model_name $name --save_per 1 `
--starting_weights $initial_w
```
