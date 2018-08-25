package com.shmut.ocr.base.enums;

/**
 * 错误码
 * 
 * @author wangpeihu
 * @date 2017/3/25
 */
public enum ErrorCode {

                       SUCCESS("SUCCESS", "成功"),

                       SYSTEM_BUSY("SYSTEM_BUSY", "系统异常，请稍后再试"),

                       SYSTEM_ERROR("SYSTEM_ERROR", "系统错误"),

                       PARAMETER_ILLEGAL("PARAMETER_ILLEGAL", "非法参数"),

                       PASSWORD_WRONG("PASSWORD_WRONG", "密码错误"),

                       USER_NOT_EXIST("USER_NOT_EXIST", "用户不存在"),

                       PASSWORD_NOT_CHANGED("PASSWORD_NOT_CHANGED", "密码未修改"),

    ;
    private String code;

    private String desc;

    public String getCode() {
        return code;
    }

    public String getDesc() {
        return desc;
    }

    ErrorCode(String code, String desc) {
        this.code = code;
        this.desc = desc;
    }

    public static ErrorCode getByCode(String code) {
        if (code == null) {
            return null;
        }
        if ("".equals(code)) {
            return null;
        }
        for (ErrorCode errorCode : values()) {
            if (errorCode.getCode().equals(code)) {
                return errorCode;
            }
        }
        return null;
    }
}
