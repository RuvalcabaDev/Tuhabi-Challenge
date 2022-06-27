CREATE TABLE `property` (
  `id` int,
  `address` varchar(120),
  `city` varchar(32),
  `price` bigint,
  `description` text(65535),
  `year` int,
  PRIMARY KEY (`id`),
  KEY `AK` (`id`)
);

CREATE TABLE `django_content_type` (
  `id` int,
  `app_label` varchar(100),
  `model` varchar(100),
  PRIMARY KEY (`id`),
  KEY `AK` (`app_label`, `model`)
);

CREATE TABLE `auth_permission` (
  `id` int,
  `name` varchar(255),
  `content_type_id` int,
  `codename` varchar(100),
  PRIMARY KEY (`id`),
  FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type`(`id`),
  KEY `AK` (`content_type_id`, `codename`)
);

CREATE TABLE `auth_group` (
  `id` int,
  `name` varchar(150),
  PRIMARY KEY (`id`),
  KEY `AK` (`name`)
);

CREATE TABLE `auth_user` (
  `id` int,
  `password` varchar(128),
  `last_login` datetime,
  `is_superuser` tinyint,
  `username` varchar(150),
  `first_name` varchar(150),
  `last_name` varchar(150),
  `email` varchar(254),
  `is_staff` tinyint,
  `is_active` tinyint,
  `date_joined` datetime,
  PRIMARY KEY (`id`),
  KEY `AK` (`username`)
);

CREATE TABLE `auth_user_groups` (
  `id` int,
  `user_id` int,
  `group_id` int,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`group_id`) REFERENCES `auth_group`(`id`),
  FOREIGN KEY (`user_id`) REFERENCES `auth_user`(`id`),
  KEY `AK` (`user_id`, `group_id`)
);

CREATE TABLE `status` (
  `id` int,
  `name` varchar(32),
  `label` varchar(64),
  PRIMARY KEY (`id`),
  KEY `AK` (`id`, `name`)
);

CREATE TABLE `status_history` (
  `id` int,
  `property_id` int,
  `status_id` int,
  `update_date` datetime,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`property_id`) REFERENCES `property`(`id`),
  FOREIGN KEY (`status_id`) REFERENCES `status`(`id`),
  KEY `AK` (`id`)
);

CREATE TABLE `auth_group_permissions` (
  `id` int,
  `group_id` int,
  `permission_id` int,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`group_id`) REFERENCES `auth_group`(`id`),
  KEY `AK` (`group_id`, `permission_id`)
);

CREATE TABLE `django_admin_log` (
  `id` int,
  `action_time` datetime,
  `object_id` longtext(4294967295),
  `object_repr` varchar(200),
  `action_flag` smallint,
  `change_message` longtext(4294967295),
  `content_type_id` int,
  `user_id` int,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type`(`id`),
  FOREIGN KEY (`user_id`) REFERENCES `auth_user`(`id`),
  FOREIGN KEY (`object_repr`) REFERENCES `auth_permission`(`id`)
);

CREATE TABLE `auth_user_user_permissions` (
  `id` int,
  `user_id` int,
  `permission_id` int,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES `auth_user`(`id`),
  FOREIGN KEY (`permission_id`) REFERENCES `auth_permission`(`id`),
  KEY `AK` (`user_id`, `permission_id`)
);

CREATE TABLE `django_migrations` (
  `id` int,
  `app` varchar(255),
  `name` varchar(255),
  `applied` datetime,
  PRIMARY KEY (`id`)
);

