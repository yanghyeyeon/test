package com.example.mongodbtest.config;

import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class MongoConfig {
    @Bean
    public MongoClient mongoClient() {
        // username, password를 실제 생성한 계정 정보로 변경
        return MongoClients.create("mongodb://test:1234@localhost:27017/test");
    }
}