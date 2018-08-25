package com.shmut.ocr;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * 箱号识别客户端启动程序
 *
 * @author wangpeihu
 * @date 2018-08-25
 */
@SpringBootApplication
public class OcrClientApplication {

    public static void main(String[] args) {
        SpringApplication.run(OcrClientApplication.class, args);
        System.out.println(">>>>>>>>>>>>>>>>>>KPI 启动完成<<<<<<<<<<<<<<<<<<<<<<<<");
    }

}
