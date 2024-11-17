package com.example.mongodbtest.controller;

import com.example.mongodbtest.entity.Chat;
import com.example.mongodbtest.repository.ChatRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/chat")
public class ChatController {

    @Autowired
    private ChatRepository chatRepository;

    @PostMapping
    public Chat createChat(@RequestBody Chat chat) {
        return chatRepository.save(chat);
    }

    @GetMapping("/{id}")
    public Chat getChat(@PathVariable String id) {
        return chatRepository.findById(id).orElse(null);
    }
}