```
!python '/content/drive/MyDrive/Senior Project/repo/food_volume_estimation/food_volume_estimation/depth_estimation/data_utils.py' \
--create_set_df \
--data_source '/content/drive/MyDrive/Senior Project/dataset/IP7_quick_out/data_sources.txt' \
--save_target '/content/drive/MyDrive/Senior Project/dataset/IP7_quick_out/df.csv' --stride 4
```

WIN train

```
$train_df = "G:\My Drive\senior-project\dataset\form\train_df.csv"
$config = "G:\My Drive\senior-project\dataset\form\config.json"
$B = 8
$E = 1
$name = "train_testing_2"
$initial_w = "C:\Source\food_volume_estimation\trained_models\train_testing_weights_epoch_6.h5"

python food_volume_estimation\depth_estimation\monovideo.py --train --train_dataframe $train_df --config $config `
--batch_size $B --training_epochs $E --model_name $name --save_per 1 `
--starting_weights $initial_w
```
