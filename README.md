
# Shipping system status by stat log

將dstat產生的系統資訊寫到Elasticsearch

## 安裝 Fluent

```
## 下載並安裝 fluentd/td-agent
curl -L https://toolbelt.treasuredata.com/sh/install-redhat-td-agent2.sh | sh
```





```
## 安裝 Elasticsearch plugin
td-agent-gem install fluent-plugin-elasticsearch
```



```
## 下載 Elasticsearch
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.2.rpm

## 安裝 Elasticsearch
rpm -i elasticsearch-5.2.2.rpm

## 啟動 Elasticsearch
systemctl start elasticsearch.service

# 測試是否成功安裝 Elasticsearch
curl http://localhost:9200/ 
```

```
## /etc/elasticsearch/elasticsearch.yml
## 修改 Elasticsearch 組態檔，在最底部加上：
network.host: 0.0.0.0
http.cors.enabled: true
http.cors.allow-origin: '*'
```


```
## 下載 fluentd/td-agent
curl -L https://toolbelt.treasuredata.com/sh/install-redhat-td-agent2.sh | sh

## 安裝 Elasticsearch plugin
td-agent-gem install fluent-plugin-elasticsearch
```


```
## 安裝 Kibana
rpm -i kibana-5.2.2-x86_64.rpm

## 啟動 Kibana
systemctl start kibana.service
```

```
## /etc/kibana/kibana.yml
## 修改 Kibana 組態檔，在最底部加上：
server.host: "0.0.0.0"
```

```
## 安裝 dstat plugin
td-agent-gem install fluent-plugin-dstat
```