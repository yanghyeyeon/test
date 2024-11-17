package com.example.mongodbtest.repository;

import com.example.mongodbtest.entity.Chat;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface ChatRepository extends MongoRepository<Chat, String> {
}
