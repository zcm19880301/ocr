package com.shmut.ocr.web;

import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;

import org.apache.commons.lang3.StringUtils;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.multipart.MultipartFile;

import lombok.extern.slf4j.Slf4j;

/**
 * 箱号识别客户端入口
 *
 * @author wangpeihu
 * @date 2018-08-25
 */
@Slf4j
@Controller
public class OcrCheckController {

    @GetMapping("/ocr/check")
    public String ocrList(ModelMap modelMap, String uploadResult) {
        if (StringUtils.isNotBlank(uploadResult)) {
            modelMap.put("uploadResult", uploadResult);
        }
        return "upload";
    }

    /**
     * OCR校验接口
     * 
     * @param files
     * @param content
     * @return
     */
    @PostMapping("/ocr/check")
    public String check(@RequestParam("files") MultipartFile[] files, String content) {
        log.info("上传的内容：{}", content);
        try {
            if (files != null) {
                for (MultipartFile file : files) {
                    if (!file.isEmpty()) {
                        String filename = file.getOriginalFilename();
                        log.info("upload file name:{}", filename);
                        file.transferTo(new File("D:/" + filename));
                    }
                }
            } else {
                return "redirect:/ocr/check?uploadResult=no file.";
            }
        } catch (IOException e) {
            log.error("save file has error. ", e);
            return "redirect:/ocr/check?uploadResult=FAILED";
        }
        return "redirect:/ocr/check?uploadResult=SUCCESS";
    }

}
