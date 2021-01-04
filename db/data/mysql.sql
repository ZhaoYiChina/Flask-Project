USE flask_project;

-- 插入用户全局注册信息
TRUNCATE TABLE `user`;
INSERT INTO `user` VALUES (1, '1', '0', '0', '0', '2017-01-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-01-11 11:01:10', '2017-01-10 23:01:05', '2017-01-11 11:01:05');
INSERT INTO `user` VALUES (2, '1', '0', '0', '0', '2017-02-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-02-11 11:01:10', '2017-01-11 01:01:05', '2017-02-11 11:01:05');
INSERT INTO `user` VALUES (3, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-01-12 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (4, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-01-13 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (5, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-01-15 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (6, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-01-15 12:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (7, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-01-16 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (8, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-01-17 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (9, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-01-18 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (10, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-01-19 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (11, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-02-01 04:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (12, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-02-01 09:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (13, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-02-12 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (14, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-03-01 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (15, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-03-02 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (16, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-03-03 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (17, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-03-04 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (18, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-03-11 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (19, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-03-11 11:01:05', '2017-03-11 11:01:05');
INSERT INTO `user` VALUES (20, '1', '0', '0', '0', '2017-03-11 11:01:10', NULL, NULL, '127.0.0.1', NULL, '2017-03-11 11:01:10', '2017-03-11 11:01:05', '2017-03-11 11:01:05');

-- 插入用户认证信息
TRUNCATE TABLE `user_auth`;
INSERT INTO `user_auth` VALUES (1, 1, 0, 'Admin', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-11 11:01:05', '2017-01-11 11:01:05');
INSERT INTO `user_auth` VALUES (2, 2, 0, 'Guest', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `user_auth` VALUES (3, 3, 0, 'Test', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (4, 1, 1, 'admin@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-11 11:01:05', '2017-01-11 11:01:05');
INSERT INTO `user_auth` VALUES (5, 2, 1, 'guest@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `user_auth` VALUES (6, 3, 1, 'test@gmail.com', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (7, 1, 2, '8613800001111', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-11 11:01:05', '2017-01-11 11:01:05');
INSERT INTO `user_auth` VALUES (8, 2, 2, '8613800002222', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `user_auth` VALUES (9, 3, 2, '8613800003333', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (10, 4, 0, 'Git', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (11, 5, 0, 'Hub', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (12, 6, 0, 'Lab', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (13, 7, 0, 'Tony', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (14, 8, 0, 'Sunny', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (15, 9, 0, 'Left', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (16, 10, 0, 'Right', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (17, 11, 0, 'Height', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (18, 12, 0, 'With', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (19, 13, 0, 'Phone', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (20, 14, 0, 'Email', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (21, 15, 0, 'Desk', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (22, 16, 0, 'Car', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (23, 17, 0, 'Mart', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (24, 18, 0, 'Light', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (25, 19, 0, 'Window', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_auth` VALUES (26, 20, 0, 'Floor', 'e10adc3949ba59abbe56e057f20f883e', '1', '2017-01-12 01:43:42', '2017-01-12 01:43:42');

-- 插入用户基本信息
TRUNCATE TABLE `user_profile`;
INSERT INTO `user_profile` VALUES (1, 0, 'Admin', 0, NULL, 'admin@gmail.com', 0, '86', '13800001111', '1900-01-01', 'Admin', '123456789098765432', '2017-01-11 11:01:05', '2017-01-11 11:01:05');
INSERT INTO `user_profile` VALUES (2, 1, 'Guest', 0, NULL, 'guest@gmail.com', 0, '86', '13800002222', '1900-01-01', 'Guest', '123456789098765433', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `user_profile` VALUES (3, 1, 'Test', 0, NULL, 'test@gmail.com', 0, '86', '13800003333', '1900-01-01', 'Test', '123456789098765434', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (4, 2, 'Git', 0, NULL, 'git@gmail.com', 0, '86', '13800004444', '1900-01-01', 'Git', '123456789098765435', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (5, 2, 'Hub', 0, NULL, 'hub@gmail.com', 0, '86', '13800005555', '1900-01-01', 'Hub', '123456789098765436', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (6, 2, 'Lab', 0, NULL, 'lab@gmail.com', 0, '86', '13800006666', '1900-01-01', 'Lab', '123456789098765437', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (7, 3, 'Tony', 0, NULL, 'tony@gmail.com', 0, '86', '13800007777', '1900-01-01', 'Tony', '123456789098765438', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (8, 3, 'Sunny', 0, NULL, 'sunny@gmail.com', 0, '86', '13800008888', '1900-01-01', 'Sunny', '123456789098765439', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (9, 3, 'Left', 0, NULL, 'left@gmail.com', 0, '86', '13800009999', '1900-01-01', 'Left', '123456789098765440', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (10, 4, 'Right', 0, NULL, 'right@gmail.com', 0, '86', '13811110000', '1900-01-01', 'Right', '123456789098765441', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (11, 4, 'Height', 0, NULL, 'height@gmail.com', 0, '86', '13811111111', '1900-01-01', 'Height', '123456789098765442', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (12, 5, 'With', 0, NULL, 'with@gmail.com', 0, '86', '13811112222', '1900-01-01', 'With', '123456789098765443', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (13, 5, 'Phone', 0, NULL, 'phone@gmail.com', 0, '86', '13811113333', '1900-01-01', 'Phone', '123456789098765444', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (14, 5, 'Email', 0, NULL, 'email@gmail.com', 0, '86', '13811114444', '1900-01-01', 'Email', '123456789098765445', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (15, 5, 'Desk', 0, NULL, 'desk@gmail.com', 0, '86', '13811115555', '1900-01-01', 'Desk', '123456789098765446', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (16, 6, 'Car', 0, NULL, 'car@gmail.com', 0, '86', '13811116666', '1900-01-01', 'Car', '123456789098765447', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (17, 7, 'Mart', 0, NULL, 'mart@gmail.com', 0, '86', '13811117777', '1900-01-01', 'Mart', '123456789098765448', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (18, 8, 'Light', 0, NULL, 'light@gmail.com', 0, '86', '13811118888', '1900-01-01', 'Light', '123456789098765449', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (19, 9, 'Window', 0, NULL, 'window@gmail.com', 0, '86', '13811119999', '1900-01-01', 'Window', '123456789098765450', '2017-01-12 01:43:42', '2017-01-12 01:43:42');
INSERT INTO `user_profile` VALUES (20, 9, 'Floor', 0, NULL, 'floor@gmail.com', 0, '86', '13822220000', '1900-01-01', 'Floor', '123456789098765451', '2017-01-12 01:43:42', '2017-01-12 01:43:42');

-- 插入用户银行信息
TRUNCATE TABLE `user_bank`;
INSERT INTO `user_bank` VALUES (1, 'Admin', '建行', '上海分行', '1234567890', 0, 0, '2017-01-11 11:01:05', '2017-01-11 11:01:05');
INSERT INTO `user_bank` VALUES (2, 'Guest', '农行', '上海分行', '1234567891', 0, 0, '2017-01-11 11:01:05', '2017-01-11 11:01:05');
INSERT INTO `user_bank` VALUES (5, 'Hub', '农行', '上海分行', '1234567892', 0, 0, '2017-01-11 11:01:05', '2017-01-11 11:01:05');
INSERT INTO `user_bank` VALUES (15, 'Desk', '农行', '上海分行', '1234567892', 0, 0, '2017-01-11 11:01:05', '2017-01-11 11:01:05');
INSERT INTO `user_bank` VALUES (19, 'Window', '农行', '上海分行', '1234567892', 0, 0, '2017-01-11 11:01:05', '2017-01-11 11:01:05');

-- 插入管理员基本信息
TRUNCATE TABLE `admin`;
INSERT INTO `admin` VALUES (1, 'admin', 'e10adc3949ba59abbe56e057f20f883e', 0, '86', '13800002222', 1, '0', NULL, NULL, NULL, '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入角色权限信息
TRUNCATE TABLE `admin_role`;
INSERT INTO `admin_role` VALUES (1, '系统', '系统角色', '会员,订单,留言,系统,权限,统计', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `admin_role` VALUES (2, '客服', '客服角色', '会员,留言,统计', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `admin_role` VALUES (3, '运营', '运营角色', '订单,留言,统计', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `admin_role` VALUES (4, '市场', '市场角色', '会员,统计', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `admin_role` VALUES (5, '销售', '销售角色', '', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `admin_role` VALUES (6, '普通', '普通角色', '', '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `admin_role` VALUES (7, '高级', '高级角色', '会员,订单,留言,统计', '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入用户声望
TRUNCATE TABLE `credit`;
INSERT INTO `credit` VALUES (1, 85, 30, 62, 50, 67, 360, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `credit` VALUES (2, 75, 40, 72, 41, 66, 360, '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入投资申请记录
TRUNCATE TABLE `apply_put`;
INSERT INTO `apply_put` VALUES (1, 1, 0, 0, 1000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:00', '2017-05-06 08:43:00');
INSERT INTO `apply_put` VALUES (2, 1, 0, 0, 2000.00, 2000.00, 1, 2, 0, null, '2017-05-06 08:43:05', '2017-05-06 08:47:07');
INSERT INTO `apply_put` VALUES (3, 1, 0, 0, 3000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:10', '2017-05-06 08:43:10');
INSERT INTO `apply_put` VALUES (4, 2, 0, 0, 1200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:39', '2017-05-06 08:43:39');
INSERT INTO `apply_put` VALUES (5, 2, 0, 0, 2200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:44', '2017-05-06 08:43:44');
INSERT INTO `apply_put` VALUES (6, 2, 0, 0, 3200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:48', '2017-05-06 08:43:48');
INSERT INTO `apply_put` VALUES (7, 3, 0, 0, 400.00, 400.00, 1, 2, 0, null, '2017-05-06 08:44:13', '2017-05-06 08:47:07');
INSERT INTO `apply_put` VALUES (8, 3, 0, 0, 600.00, 0.00, 1, 0, 0, null, '2017-05-06 08:44:17', '2017-05-06 08:44:17');
INSERT INTO `apply_put` VALUES (9, 3, 0, 0, 800.00, 800.00, 1, 2, 0, null, '2017-05-06 08:44:21', '2017-05-06 08:47:07');
INSERT INTO `apply_put` VALUES (10, 15, 0, 0, 2000.00, 2000.00, 1, 2, 0, null, '2017-05-06 08:44:21', '2017-05-06 08:47:07');

-- 插入提现申请记录
TRUNCATE TABLE `apply_get`;
INSERT INTO `apply_get` VALUES (1, 1, 0, 0, 0, 1000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:15', '2017-05-06 08:43:15');
INSERT INTO `apply_get` VALUES (2, 1, 0, 0, 0, 2000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:22', '2017-05-06 08:43:22');
INSERT INTO `apply_get` VALUES (3, 1, 0, 0, 0, 3000.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:27', '2017-05-06 08:43:27');
INSERT INTO `apply_get` VALUES (4, 2, 0, 0, 0, 1200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:53', '2017-05-06 08:43:53');
INSERT INTO `apply_get` VALUES (5, 2, 0, 0, 0, 2200.00, 0.00, 1, 0, 0, null, '2017-05-06 08:43:58', '2017-05-06 08:43:58');
INSERT INTO `apply_get` VALUES (6, 2, 0, 0, 0, 3200.00, 3200.00, 1, 2, 0, null, '2017-05-06 08:44:02', '2017-05-06 08:47:07');
INSERT INTO `apply_get` VALUES (7, 3, 0, 0, 0, 400.00, 0.00, 1, 0, 0, null, '2017-05-06 08:44:25', '2017-05-06 08:44:25');
INSERT INTO `apply_get` VALUES (8, 3, 0, 0, 0, 600.00, 0.00, 1, 0, 0, null, '2017-05-06 08:44:28', '2017-05-06 08:44:28');
INSERT INTO `apply_get` VALUES (9, 3, 0, 0, 0, 800.00, 0.00, 1, 0, 0, null, '2017-05-06 08:44:32', '2017-05-06 08:44:32');
INSERT INTO `apply_get` VALUES (10, 19, 0, 0, 0, 2000.00, 2000.00, 1, 2, 0, null, '2017-05-06 08:44:32', '2017-05-06 08:44:32');


-- 插入订单记录
TRUNCATE TABLE `order`;
INSERT INTO `order` VALUES (1, 2, 6, 1, 2, 0, 2000.00, 1, 0, 0, 0, 0, '2017-05-06 08:47:07', null, null, null, '2017-05-06 08:47:07', '2017-05-06 08:47:07');
INSERT INTO `order` VALUES (2, 7, 6, 3, 2, 0, 400.00, 1, 0, 0, 0, 0, '2017-05-06 08:47:07', null, null, null, '2017-05-06 08:47:07', '2017-05-06 08:47:07');
INSERT INTO `order` VALUES (3, 9, 6, 3, 2, 0, 800.00, 1, 0, 0, 0, 0, '2017-05-06 08:47:07', null, null, null, '2017-05-06 08:47:07', '2017-05-06 08:47:07');
INSERT INTO `order` VALUES (4, 10, 10, 15, 19, 0, 2000.00, 1, 0, 1, 1, 0, '2017-05-06 08:47:07', null, null, null, '2017-05-06 08:47:07', '2017-05-06 08:47:07');

-- 插入订单凭证
TRUNCATE TABLE `order_bill`;

-- 插入钱包总表
TRUNCATE TABLE `wallet`;
INSERT INTO `wallet` VALUES (1, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (2, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (3, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (4, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (5, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (6, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (7, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (8, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (9, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (10, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (11, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (12, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (13, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (14, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (15, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (16, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (17, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (18, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (19, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (20, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (21, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `wallet` VALUES (22, '10000.00', '24000.00', 0, '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入钱包明细
TRUNCATE TABLE `wallet_item`;

-- 插入积分总表
TRUNCATE TABLE `score`;
INSERT INTO `score` VALUES (1, '0.00', '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入积分明细
TRUNCATE TABLE `score_item`;

-- 插入慈善积分总表
TRUNCATE TABLE `score_charity`;

-- 插入慈善积分明细
TRUNCATE TABLE `score_charity_item`;
INSERT INTO `score_charity_item` VALUES (1, 1, 1, '10.00', 0, '测试获得积分', 1, 0, '2017-01-12 12:25:34', NULL, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `score_charity_item` VALUES (2, 1, 2, '5.00', 0, '测试消费积分', 1, 0, '2017-01-12 12:25:34', NULL, '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入数字积分总表
TRUNCATE TABLE `score_digital`;

-- 插入数字积分明细
TRUNCATE TABLE `score_digital_item`;

-- 插入消费积分总表
TRUNCATE TABLE `score_expense`;

-- 插入消费积分明细
TRUNCATE TABLE `score_expense_item`;

-- 插入奖金总表
TRUNCATE TABLE `bonus`;
INSERT INTO `bonus` VALUES (1, '0.00', '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入奖金明细
TRUNCATE TABLE `bonus_item`;

-- 插入数字货币总表
TRUNCATE TABLE `bit_coin`;

-- 插入数字货币明细
TRUNCATE TABLE `bit_coin_item`;

-- 插入激活总表
TRUNCATE TABLE `active`;
INSERT INTO `active` VALUES (1, 5, '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入激活明细
TRUNCATE TABLE `active_item`;
INSERT INTO `active_item` VALUES (1, 0, 2, 10, 1, '', 1, 0, '2017-01-12 12:25:34', NULL, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `active_item` VALUES (2, 1, 2, 2, 2, '', 1, 0, '2017-01-12 12:25:34', NULL, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `active_item` VALUES (3, 1, 1, 1, 3, '', 1, 0, '2017-01-12 12:25:34', NULL, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `active_item` VALUES (4, 1, 2, 1, 3, '', 1, 0, '2017-01-12 12:25:34', NULL, '2017-01-12 12:25:34', '2017-01-12 12:25:34');
INSERT INTO `active_item` VALUES (5, 1, 2, 1, 4, '', 1, 0, '2017-01-12 12:25:34', NULL, '2017-01-12 12:25:34', '2017-01-12 12:25:34');

-- 插入留言消息
TRUNCATE TABLE `message`;
INSERT INTO `message` VALUES (1, 1, 2, '测试消息', 0, null, '2017-06-24 13:23:27', '2017-06-24 13:23:27');

-- 插入投诉消息
TRUNCATE TABLE `complaint`;
INSERT INTO `complaint` VALUES (1, 1, 2, 0, '测试消息', '', 0, null, 0, null, '2017-06-24 13:23:27', '2017-06-24 13:23:27');

-- 插入用户配置信息
TRUNCATE TABLE `user_config`;
INSERT INTO `user_config` VALUES (1, '0.10,0.10,0.10', '2017-06-24 13:23:27', '2017-06-24 13:23:27');

-- 插入排单币总表
TRUNCATE TABLE `scheduling`;
INSERT INTO `scheduling` VALUES (1, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (2, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (3, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (4, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (5, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (6, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (7, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (8, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (9, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (10, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (11, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (12, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (13, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (14, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (15, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (16, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (17, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (18, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (19, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (20, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (21, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');
INSERT INTO `scheduling` VALUES (22, 100.00, '2017-06-29 18:27:01', '2017-06-29 18:27:01');

-- 插入排单币明细表
TRUNCATE TABLE `scheduling_item`;
INSERT INTO `scheduling_item` VALUES (1, 0, 2, 100, 1, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (2, 0, 2, 100, 2, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (3, 0, 2, 100, 3, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (4, 0, 2, 100, 4, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (5, 0, 2, 100, 5, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (6, 0, 2, 100, 6, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (7, 0, 2, 100, 7, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (8, 0, 2, 100, 8, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (9, 0, 2, 100, 9, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (10, 0, 2, 100, 10, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (11, 0, 2, 100, 11, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (12, 0, 2, 100, 12, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (13, 0, 2, 100, 13, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (14, 0, 2, 100, 14, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (15, 0, 2, 100, 15, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (16, 0, 2, 100, 16, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (17, 0, 2, 100, 17, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (18, 0, 2, 100, 18, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (19, 0, 2, 100, 19, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (20, 0, 2, 100, 20, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (21, 0, 2, 100, 21, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
INSERT INTO `scheduling_item` VALUES (22, 0, 2, 100, 22, '', 1, 0, '2017-06-29 17:24:36', null, '2017-06-29 17:24:36', '2017-06-29 17:24:36');
