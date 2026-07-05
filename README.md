Django API 容器化實作專案 
## 專案簡介

本專案為一個基於 Django 與 Django REST Framework  的 API 練習專案。目標是實現待辦事項  的管理功能，並透過 Docker 容器化技術，將應用程式與 MySQL 資料庫環境封裝，確保開發與部署的一致性。
---
## 技術棧 

    後端: Django 5.2.15, Django REST Framework

    資料庫: MySQL 8.0

    部署與環境: Docker, Docker Compose, Linux (Ubuntu)

---
## 執行結果
可以看到使用者登入畫面

<img width="624" height="486" alt="image" src="https://github.com/user-attachments/assets/7e44c23e-cde9-4897-9af8-8d17b7183f73" />


<img width="666" height="344" alt="image" src="https://github.com/user-attachments/assets/a43bc3e5-4567-40ac-9c77-a3416c61867a" />

---
## 開發心得與技術挑戰

在本次部署過程中，我深刻體會到「環境一致性」對開發者的重要性。將專案從本機轉移至 Docker 容器的過程，遠比預期中充滿挑戰，但也讓我累積了許多寶貴的 Debug 經驗：
1. 服務啟動順序的處理

困難: Django App 啟動時，MySQL 容器尚未完全就緒，導致頻繁出現 OperationalError 連線錯誤。
克服: 我在 docker-compose.yml 中加入了 nc 檢查邏輯（或改用 Python socket 測試），強制 App 等待資料庫的 3306 埠開啟後才執行 migrate 與啟動伺服器，確保了服務的啟動順序。
2. 環境與容器間的衝突

困難: 頻繁修改配置檔與強行中斷執行，導致 Docker 內部的 metadata 殘留，產生 KeyError: 'id' 錯誤。
克服: 學習使用 sudo docker-compose down -v 徹底清理匿名卷 (Volume)，並搭配 sudo docker system prune -f 移除系統垃圾，成功解決了快取狀態不一致的問題。
3. 安全性設定與權限管理

困難: Django 出於安全性考慮，拒絕了來自 Docker 網路的外部存取 (DisallowedHost)。
克服: 透過正確設定 ALLOWED_HOSTS 並精確管理 superuser 權限，成功打通了從瀏覽器到容器內部的存取路徑。
功能驗證

    Admin 後台: http://localhost:8000/admin/ (帳號: rhys)

    API 接口: http://localhost:8000/api/todos/
    

    Clone 此專案。

    執行 sudo docker-compose up -d --build 啟動服務。

    執行 sudo docker-compose exec app python manage.py createsuperuser 建立管理權限。


