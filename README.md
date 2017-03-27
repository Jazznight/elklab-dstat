
# Shipping system status by stat log

 1. [將dstat產生的系統數據透過Fluentd傳送](./docs/step1.md)
 2. [將dstat產生的系統數據透過Fluentd做資料轉換](./docs/step2.md)
 3. [將dstat產生的系統數據透過Fluentd轉存Elasticsearch](./docs/step3.md)
 4. 將轉存的dstat系統數據透過Kibana繪製圖表

dstat LOG | Elasticsearch store
--- | ---
![dstat output](http://i.imgur.com/3ACAm2o.png) | ![a](http://i.imgur.com/9H53LW3.png)


# 環境準備

## Fluentd

下載並安裝 Fluentd
```shell
curl -L https://toolbelt.treasuredata.com/sh/install-redhat-td-agent2.sh | sh
```

安裝 dstat input plugin
```shell
td-agent-gem install fluent-plugin-dstat
```

<br>

## Elasticsearch


下載 Elasticsearch
```shell
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.2.rpm
```

安裝Elasticsearch
```shell
rpm -i elasticsearch-5.2.2.rpm
```

測試是否成功安裝 Elasticsearch
```shell
curl http://localhost:9200/
```

安裝 Elasticsearch output plugin

```shell
td-agent-gem install fluent-plugin-elasticsearch`
```

組態 Elasticsearch(`/etc/elasticsearch/elasticsearch.yml`)，在最底部加上：
```shell
network.host: 0.0.0.0
http.cors.enabled: true
http.cors.allow-origin: '*'
```

啟動 Elasticsearch
```shell
systemctl start elasticsearch.service
```

<br>

## Kibana

安裝 Kibana

```shell
rpm -i kibana-5.2.2-x86_64.rpm
```

組態 Kibana(`/etc/kibana/kibana.ym`)，在最底部加上：
```shell
server.host: "0.0.0.0"
```

啟動 Kibana
```
systemctl start kibana.service
```