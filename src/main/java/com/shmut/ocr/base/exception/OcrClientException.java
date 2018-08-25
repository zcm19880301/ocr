package com.shmut.ocr.base.exception;

import com.shmut.ocr.base.enums.ErrorCode;

/**
 * 异常定义
 *
 * @author wangpeihu
 * @date 2018-08-25
 */
public class OcrClientException extends RuntimeException {

    private ErrorCode errorCode;

    public ErrorCode getErrorCode() {
        return errorCode;
    }

    public OcrClientException setErrorCode(ErrorCode errorCode) {
        this.errorCode = errorCode;
        return this;
    }

    public OcrClientException(ErrorCode errorCode, Throwable cause) {
        super(cause);
        this.errorCode = errorCode;
    }

    public OcrClientException(ErrorCode errorCode) {
        this.errorCode = errorCode;
    }
}
