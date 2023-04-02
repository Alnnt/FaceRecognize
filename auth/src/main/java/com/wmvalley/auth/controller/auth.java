package com.wmvalley.auth.controller;

import com.wmvalley.auth.entity.Check;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.multipart.MultipartFile;

@CrossOrigin
@RestController
@RequestMapping("/auth")
public class auth {
    @PostMapping("/face")
    public String face(@RequestBody Check data){
        System.out.println(data.uid);
        System.out.println(data.img);
        return "face";
    }
}
