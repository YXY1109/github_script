/*
 Navicat Premium Data Transfer

 Source Server         : 243
 Source Server Type    : MySQL
 Source Server Version : 100427
 Source Host           : 192.168.180.243:3306
 Source Schema         : wx_article

 Target Server Type    : MySQL
 Target Server Version : 100427
 File Encoding         : 65001

 Date: 20/02/2024 15:45:08
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for article
-- ----------------------------
DROP TABLE IF EXISTS `article`;
CREATE TABLE `article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `url` varchar(255) NOT NULL,
  `create_time` datetime NOT NULL,
  `update_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1092 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- ----------------------------
-- Records of article
-- ----------------------------
BEGIN;
INSERT INTO `article` VALUES (1, '鸟哥笔记', '2024年，游戏厂商再不重视小红书就晚了', 'https://mp.weixin.qq.com/s/XjoLMZUQ1rlC_SSubXTAaA', '2024-01-29 15:26:31', '2024-01-29 15:26:31');
INSERT INTO `article` VALUES (2, '鸟哥笔记', '年入百万or吃不上饭，短剧成网文作者的下一个战场？', 'https://mp.weixin.qq.com/s/zUYvHZQjkX3r0163VcsP-w', '2024-01-29 15:26:31', '2024-01-29 15:26:31');
INSERT INTO `article` VALUES (3, '鸟哥笔记', '一周资讯京东成为春晚独家互动合作平台；马云成阿里巴巴最大股东；闲鱼微信..', 'https://mp.weixin.qq.com/s/rE-sFy1IYdvY5vjqUgoS4w', '2024-01-29 15:26:31', '2024-01-29 15:26:31');
INSERT INTO `article` VALUES (4, '鸟哥笔记', '企业痛难点一站式线下培训解决方案', 'https://mp.weixin.qq.com/s/7RXl0n2FtwixtC4-0ijtnw', '2024-01-29 15:26:31', '2024-01-29 15:26:31');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
