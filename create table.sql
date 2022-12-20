DROP TABLE gui_table
-- Create the table in the specified schema
CREATE TABLE gui_table
(
    id INT NOT NULL PRIMARY KEY, 
    ФИО VARCHAR(200) NOT NULL,
    Возраст INT NOT NULL,
    Семейный_статус VARCHAR(50) NOT NULL,
    Звание VARCHAR(50) NOT NULL UNIQUE
)

INSERT INTO public.gui_table (id, ФИО, Возраст, Семейный_статус, Звание) VALUES (1, 'Клепиков Никита Михайлович', '27', 'Холост', 'Лейтенант');
INSERT INTO public.gui_table (id, ФИО, Возраст, Семейный_статус, Звание) VALUES (2, 'Шляпников Павел Анатольевич', '34', 'Женат', 'Майор');
INSERT INTO public.gui_table (id, ФИО, Возраст, Семейный_статус, Звание) VALUES (3, 'Одобеску Виктор Трофимович', '45', 'Женат', 'Полковник');
INSERT INTO public.gui_table (id, ФИО, Возраст, Семейный_статус, Звание) VALUES (4, 'Козырев Дмитрий Константинович', '20', 'Холост', 'Рядовой');