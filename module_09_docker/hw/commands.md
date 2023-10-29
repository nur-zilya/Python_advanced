1) $ docker start gifted_ellis #запускаем контейнер

2) $ docker exec -it <id_контейнера> uptime #Запустить команду docker exec в интерактивном режиме для уже запущенного контейнера, чтобы выполнить команду uptime.
    Узнать id можно командой docker ps

3) docker exec -it <id_контейнера> /bin/bash  #войти в контейнер 

4) sudo apt-get update #обновить пакеты

5) sudo apt-get install htop #установить htop (сколько памяти потребляет система внутри контейнера)

6) which htop #узнать куда установился htop