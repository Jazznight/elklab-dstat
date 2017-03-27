
## 將dstat產生的系統數據透過Fluentd做資料轉換

透過組態 Fluentd [conf/step-transform.conf](../conf/step-transform.conf)，並執行td-agent
```shell
./run.sh conf/conf/step-transform.conf
```