package com.example.test.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

@RestController
public class DemoController {
    @GetMapping()
    public Map<String, Object> index() {
        Map<String, Object> map = new HashMap<>();
        map.put("id", UUID.randomUUID());
        map.put("time", System.currentTimeMillis());
        return map;
    }
}
