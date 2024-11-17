package com.example.mongodbtest.entity;

import lombok.Data;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Data
@Document(collection = "test")
public class Chat {

    @Id
    private String id;
    private String chatId;
    private String userId; // 회원일 경우 사용자 ID
    private String guestId; // 비회원일 경우 임시 ID
    private String sender; // "user" 또는 "bot"
    private String message;
    private String timestamp;
}
