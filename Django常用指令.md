Django 提供了许多命令行工具（通过 `python manage.py` 调用），用于开发、测试和管理项目。以下是最常用的 Django 指令及其功能：

---

### 1. **项目相关指令**
#### `startproject`
- **功能**：创建一个新的 Django 项目。
- **示例**：
  ```bash
  django-admin startproject myproject
  ```

#### `startapp`
- **功能**：在项目中创建一个新的应用。
- **示例**：
  ```bash
  python manage.py startapp myapp
  ```

---

### 2. **开发服务器指令**
#### `runserver`
- **功能**：启动 Django 开发服务器，用于本地开发。
- **示例**：
  ```bash
  python manage.py runserver
  ```
  指定端口：
  ```bash
  python manage.py runserver 8080
  ```

---

### 3. **数据库相关指令**
#### `makemigrations`
- **功能**：根据模型的变更生成数据库迁移文件。
- **示例**：
  ```bash
  python manage.py makemigrations
  ```

#### `migrate`
- **功能**：将迁移文件应用到数据库，更新数据库结构。
- **示例**：
  ```bash
  python manage.py migrate
  ```

#### `sqlmigrate`
- **功能**：查看某个迁移文件对应的 SQL 语句。
- **示例**：
  ```bash
  python manage.py sqlmigrate myapp 0001_initial
  ```

#### `showmigrations`
- **功能**：显示项目中所有应用的迁移状态。
- **示例**：
  ```bash
  python manage.py showmigrations
  ```

#### `flush`
- **功能**：清空数据库中的所有数据，保留表结构。
- **示例**：
  ```bash
  python manage.py flush
  ```

#### `dbshell`
- **功能**：打开数据库的交互式 shell。
- **示例**：
  ```bash
  python manage.py dbshell
  ```

---

### 4. **管理员相关指令**
#### `createsuperuser`
- **功能**：创建一个超级用户，用于访问 Django 管理后台。
- **示例**：
  ```bash
  python manage.py createsuperuser
  ```

#### `changepassword`
- **功能**：修改用户的密码。
- **示例**：
  ```bash
  python manage.py changepassword username
  ```

---

### 5. **静态文件相关指令**
#### `collectstatic`
- **功能**：收集所有静态文件到 `STATIC_ROOT` 目录。
- **示例**：
  ```bash
  python manage.py collectstatic
  ```

---

### 6. **测试相关指令**
#### `test`
- **功能**：运行项目的测试用例。
- **示例**：
  ```bash
  python manage.py test
  ```
  测试指定应用：
  ```bash
  python manage.py test myapp
  ```

#### `testserver`
- **功能**：使用测试数据库启动开发服务器。
- **示例**：
  ```bash
  python manage.py testserver myfixture.json
  ```

---

### 7. **国际化相关指令**
#### `makemessages`
- **功能**：提取模板和代码中的翻译字符串，生成 `.po` 文件。
- **示例**：
  ```bash
  python manage.py makemessages -l zh_Hans
  ```

#### `compilemessages`
- **功能**：将 `.po` 文件编译为 `.mo` 文件。
- **示例**：
  ```bash
  python manage.py compilemessages
  ```

---

### 8. **其他常用指令**
#### `shell`
- **功能**：启动 Django 的交互式 shell，可以访问项目的模型和配置。
- **示例**：
  ```bash
  python manage.py shell
  ```

#### `check`
- **功能**：检查项目是否有常见错误或问题。
- **示例**：
  ```bash
  python manage.py check
  ```

#### `shell_plus`
- **功能**：启动增强版的 Django shell（需要安装 `django-extensions`）。
- **示例**：
  ```bash
  python manage.py shell_plus
  ```

#### `runscript`
- **功能**：运行自定义的 Python 脚本（需要安装 `django-extensions`）。
- **示例**：
  ```bash
  python manage.py runscript myscript
  ```

---

### 9. **扩展指令**
#### `graph_models`
- **功能**：生成项目的 ER 图（需要安装 `django-extensions` 和 `pygraphviz`）。
- **示例**：
  ```bash
  python manage.py graph_models -a -o myproject_models.png
  ```

#### `export_emails`
- **功能**：导出所有用户的电子邮件地址（需要安装 `django-extensions`）。
- **示例**：
  ```bash
  python manage.py export_emails -f emails.txt
  ```

---

### 总结
Django 的常用指令涵盖了项目开发、数据库管理、测试、静态文件处理等多个方面。以下是核心指令：
- **项目创建**：`startproject`, `startapp`
- **开发服务器**：`runserver`
- **数据库管理**：`makemigrations`, `migrate`
- **管理员操作**：`createsuperuser`, `changepassword`
- **测试**：`test`
- **静态文件**：`collectstatic`
