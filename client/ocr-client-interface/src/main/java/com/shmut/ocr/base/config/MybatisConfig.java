package com.shmut.ocr.base.config;

import java.util.Properties;

import javax.sql.DataSource;

import org.apache.ibatis.plugin.Interceptor;
import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.SqlSessionFactoryBean;
import org.mybatis.spring.annotation.MapperScan;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;
import org.springframework.core.io.support.PathMatchingResourcePatternResolver;

import com.alibaba.druid.pool.DruidDataSourceFactory;
import com.github.pagehelper.PageInterceptor;

/**
 * 数据库及mybaits配置中心
 * 
 * @author wangpeihu
 */
@Configuration
@MapperScan("com.shmut.ocr.dal.mapper")
public class MybatisConfig {

    /** 环境变量 */
    @Autowired
    private Environment env;

    /** 数据库用户名 */
    @Value("${db.username}")
    private String      username;

    /** 数据库密码*/
    @Value("${db.password}")
    private String      password;

    /** 数据库连接url*/
    @Value("${db.url}")
    private String      url;

    /**
     * 创建DataSource
     * 
     * @return
     * @throws Exception
     */
    @Bean
    public DataSource getDataSource() throws Exception {
        Properties props = new Properties();
        props.put("driverClassName", env.getProperty("spring.datasource.driver-class-name"));
        props.put("url", url);
        props.put("username", username);
        props.put("password", password);
        return DruidDataSourceFactory.createDataSource(props);
    }

    /**
     * 创建SqlSessionFactory
     * 
     * @return
     * @throws Exception
     */
    @Bean
    public SqlSessionFactory sqlSessionFactory() throws Exception {
        SqlSessionFactoryBean sessionFactory = new SqlSessionFactoryBean();
        sessionFactory.setDataSource(getDataSource());
        sessionFactory.setTypeAliasesPackage(env.getProperty("mybatis.type-aliases-package"));
        sessionFactory.setMapperLocations(new PathMatchingResourcePatternResolver()
            .getResources(env.getProperty("mybatis.mapper-locations")));

        PageInterceptor pageInterceptor = new PageInterceptor();
        Properties properties = new Properties();
        properties.put("params", "value1");
        pageInterceptor.setProperties(properties);
        sessionFactory.setPlugins(new Interceptor[] { pageInterceptor });

        return sessionFactory.getObject();
    }
}
