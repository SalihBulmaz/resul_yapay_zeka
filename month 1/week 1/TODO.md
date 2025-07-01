# 1. Ay 1. Hafta - Pandas Öğrenme Todo Listesi

> **Hedef:** 20 saat/hafta | **Teorik:** 8-10 saat | **Pratik:** 10-12 saat

---

## 📅 1. GÜN - PAZARTESİ (3 saat)

### 🎯 Günün Hedefi: Pandas Temelleri ve Kurulum

#### Teorik Çalışma (1.5 saat)
- [x] **Pandas teorik eğitim dökümanını oku** (45 dk)
  - [ ] Pandas'ın rolü ve önemi bölümü
  - [ ] Veri yapıları: Series ve DataFrame
  - [ ] Excel vs Pandas karşılaştırması
- [ ] **Video izle:** "Pandas Introduction" (45 dk)
  - [ ] Önerilen: Corey Schafer - Pandas Tutorial #1
  - [ ] Not al: Neden Pandas kullanıyoruz?

#### Pratik Çalışma (1.5 saat)
- [ ] **Geliştirme ortamını hazırla** (30 dk)
  - [ ] Python ve Pandas kurulumunu kontrol et
  - [ ] Jupyter Notebook veya VS Code hazırla
  - [ ] İlk import pandas as pd testini yap
- [ ] **İlk DataFrame oluştur** (60 dk)
  - [ ] 5 şehir bilgisi ile DataFrame oluştur
  - [ ] Series kavramını test et
  - [ ] Basic info() ve describe() fonksiyonlarını dene
  - [ ] shape, columns, index özelliklerini keşfet

#### Günün Kontrolü
- [ ] Pandas'ın ne olduğunu kendi cümlelerinle açıklayabiliyorsun
- [ ] Series ve DataFrame arasındaki farkı biliyorsun
- [ ] İlk DataFrame'ini başarıyla oluşturdun

---

## 📅 2. GÜN - SALI (3 saat)

### 🎯 Günün Hedefi: Veri Okuma ve Yazma İşlemleri

#### Teorik Çalışma (1 saat)
- [ ] **Teorik döküman:** Veri okuma/yazma bölümü (30 dk)
  - [ ] CSV vs Excel farkları
  - [ ] Encoding kavramı (özellikle Türkçe karakterler)
- [ ] **Video izle:** "Reading and Writing Data" (30 dk)
  - [ ] Önerilen: Data School - Pandas read_csv

#### Pratik Çalışma (2 saat)
- [ ] **CSV İşlemleri** (60 dk)
  - [ ] Örnek CSV dosyası oluştur (en az 10 satır veri)
  - [ ] read_csv() ile dosyayı oku
  - [ ] Farklı parametreleri dene (encoding, sep, header)
  - [ ] to_csv() ile farklı ayarlarla kaydet
- [ ] **Excel İşlemleri** (30 dk)
  - [ ] openpyxl kütüphanesini kur
  - [ ] Excel dosyası oluştur ve oku
  - [ ] read_excel() parametrelerini keşfet
- [ ] **Gerçek Veri İndir** (30 dk)
  - [ ] Kaggle'dan basit bir CSV dataset indir
  - [ ] Bu veriyi Pandas ile aç
  - [ ] İlk keşif: head(), tail(), info(), describe()

#### Günün Kontrolü
- [ ] CSV dosyalarını problemsiz okuyup yazabiliyorsun
- [ ] Encoding sorunlarını çözebiliyorsun
- [ ] Gerçek bir veri setini açıp inceleyebildin

---

## 📅 3. GÜN - ÇARŞAMBA (3 saat)

### 🎯 Günün Hedefi: Veri Seçimi ve Filtreleme

#### Teorik Çalışma (1 saat)
- [ ] **Teorik döküman:** İndeksleme ve filtreleme bölümü (30 dk)
  - [ ] loc vs iloc farkı
  - [ ] Boolean indexing mantığı
- [ ] **Video izle:** "Data Selection and Filtering" (30 dk)
  - [ ] Önerilen: Corey Schafer - Pandas Tutorial #3

#### Pratik Çalışma (2 saat)
- [ ] **Temel Seçim İşlemleri** (60 dk)
  - [ ] Tek sütun seçimi (Series vs DataFrame)
  - [ ] Birden fazla sütun seçimi
  - [ ] iloc ile pozisyon bazlı seçim
  - [ ] loc ile label bazlı seçim
  - [ ] İlk/son N satır seçimi
- [ ] **Boolean Filtreleme** (60 dk)
  - [ ] Tek koşul ile filtreleme (sayısal ve string)
  - [ ] İki koşul ile filtreleme (& ve | operatörleri)
  - [ ] isin() fonksiyonu ile filtreleme
  - [ ] NOT (~) operatörü ile ters filtreleme
  - [ ] Karmaşık filtreleme kombinasyonları dene

#### Günün Kontrolü
- [ ] loc ve iloc arasındaki farkı anlıyorsun
- [ ] Boolean filtreleme ile istediğin verileri seçebiliyorsun
- [ ] Karmaşık koşulları & ve | ile birleştirebiliyorsun

---

## 📅 4. GÜN - PERŞEMBE (3 saat)

### 🎯 Günün Hedefi: Veri Temizleme

#### Teorik Çalışma (1 saat)
- [ ] **Teorik döküman:** Veri temizleme bölümü (30 dk)
  - [ ] Eksik veri türleri (NaN, None, NaT)
  - [ ] Eksik veri işleme stratejileri
- [ ] **Video izle:** "Handling Missing Data" (30 dk)
  - [ ] Önerilen: Data School - Handling missing data

#### Pratik Çalışma (2 saat)
- [ ] **Eksik Veri İşleme** (90 dk)
  - [ ] Bilinçli olarak eksik veri oluştur
  - [ ] isnull() ve notnull() fonksiyonlarını kullan
  - [ ] Eksik veri sayısını hesapla
  - [ ] dropna() ile eksik verileri sil
  - [ ] fillna() ile eksik verileri doldur
  - [ ] Farklı doldurma stratejilerini dene (mean, median, mode)
  - [ ] Forward fill ve backward fill yöntemlerini test et
- [ ] **Tekrarlanan Veri İşleme** (30 dk)
  - [ ] Bilinçli olarak tekrarlanan veri oluştur
  - [ ] duplicated() ile tekrarları tespit et
  - [ ] drop_duplicates() ile tekrarları sil
  - [ ] Subset parametresi ile kısmi tekrar kontrolü

#### Günün Kontrolü
- [ ] Eksik verileri tespit edip uygun yöntemle işleyebiliyorsun
- [ ] Tekrarlanan verileri bulup temizleyebiliyorsun
- [ ] Hangi durumda hangi temizleme yöntemini kullanacağını biliyorsun

---

## 📅 5. GÜN - CUMA (3 saat)

### 🎯 Günün Hedefi: Veri Dönüştürme ve Gruplama

#### Teorik Çalışma (1 saat)
- [ ] **Teorik döküman:** Gruplama ve dönüştürme bölümü (30 dk)
  - [ ] Split-apply-combine paradigması
  - [ ] Apply fonksiyonlarının mantığı
- [ ] **Video izle:** "GroupBy Operations" (30 dk)
  - [ ] Önerilen: Corey Schafer - Pandas Tutorial #7

#### Pratik Çalışma (2 saat)
- [ ] **Yeni Sütun Oluşturma** (45 dk)
  - [ ] Matematiksel işlemlerle yeni sütun oluştur
  - [ ] apply() fonksiyonu ile özel işlemler
  - [ ] Lambda fonksiyonları ile kısa işlemler
  - [ ] String işlemleri ile yeni sütunlar
- [ ] **Gruplama İşlemleri** (75 dk)
  - [ ] groupby() ile temel gruplama
  - [ ] Tek sütuna göre gruplama ve agregasyon
  - [ ] Birden fazla sütuna göre gruplama
  - [ ] size(), count(), sum(), mean() fonksiyonları
  - [ ] agg() ile özel agregasyon fonksiyonları
  - [ ] Pivot table oluşturma

#### Günün Kontrolü
- [ ] Apply fonksiyonlarını kullanabiliyorsun
- [ ] GroupBy ile veriyi gruplayıp analiz edebiliyorsun
- [ ] Pivot table oluşturabiliyorsun

---

## 📅 6. GÜN - CUMARTESİ (2.5 saat)

### 🎯 Günün Hedefi: Sıralama ve İndeksleme

#### Teorik Çalışma (30 dk)
- [ ] **Teorik döküman:** İndeksleme bölümünü tekrar oku
  - [ ] Index kavramını pekiştir
  - [ ] MultiIndex kavramını öğren

#### Pratik Çalışma (2 saat)
- [ ] **Sıralama İşlemleri** (45 dk)
  - [ ] sort_values() ile tek sütuna göre sıralama
  - [ ] Birden fazla sütuna göre sıralama
  - [ ] Ascending/descending kombinasyonları
  - [ ] sort_index() ile index bazlı sıralama
- [ ] **İndeks İşlemleri** (75 dk)
  - [ ] set_index() ile yeni index belirleme
  - [ ] reset_index() ile index sıfırlama
  - [ ] MultiIndex oluşturma ve kullanma
  - [ ] Index ile veri seçimi
  - [ ] reindex() ile index yeniden düzenleme

#### Günün Kontrolü
- [ ] Veriyi istediğin kriterlere göre sıralayabiliyorsun
- [ ] Index kavramını anlıyor ve yönetebiliyorsun
- [ ] MultiIndex ile çalışabiliyorsun

---

## 📅 7. GÜN - PAZAR (2.5 saat)

### 🎯 Günün Hedefi: Kapsamlı Pratik ve Hafta Değerlendirmesi

#### Büyük Proje (2 saat)
- [ ] **100 Satırlık Veri Seti Projesi**
  - [ ] 100 kişilik çalışan verisi oluştur
  - [ ] Bilinçli olarak eksik ve tekrarlanan veri ekle
  - [ ] Veriyi temizle
  - [ ] Departman bazlı analiz yap
  - [ ] Yaş grubu analizi yap
  - [ ] Maaş dağılımı analizi yap
  - [ ] En yüksek/düşük performans analizleri
  - [ ] Pivot table ile özet çıkar
  - [ ] Sonuçları CSV ve Excel'e kaydet

#### Hafta Değerlendirmesi (30 dk)
- [ ] **Kendini Test Et**
  - [ ] Bu haftanın 10 ana konusunu listele
  - [ ] Her konudan bir örnek kod yaz
  - [ ] Hangi konularda zorlandığını belirle
  - [ ] Gelecek hafta için öncelik listesi oluştur

---

## 🎯 HAFTALIK HEDEFLERİN KONTROLÜ

### Temel Beceriler
- [ ] Pandas kütüphanesini import edip kullanabiliyorum
- [ ] CSV ve Excel dosyalarını okuyup yazabiliyorum
- [ ] DataFrame ve Series arasındaki farkı biliyorum
- [ ] Veri seçimi ve filtreleme işlemlerini yapabiliyorum
- [ ] Eksik verileri tespit edip uygun yöntemle işleyebiliyorum

### İleri Beceriler
- [ ] Boolean indexing ile karmaşık filtreler yazabiliyorum
- [ ] GroupBy ile veriyi gruplayıp analiz edebiliyorum
- [ ] Apply fonksiyonları ile özel işlemler yapabiliyorum
- [ ] Pivot table oluşturabiliyorum
- [ ] Index işlemlerini yönetebiliyorum

### Proje Becerileri
- [ ] 100+ satırlık veri setiyle çalışabiliyorum
- [ ] End-to-end veri analizi süreci yapabiliyorum
- [ ] Sonuçları farklı formatlarda kaydedebiliyorum
- [ ] Veri kalitesi sorunlarını çözebiliyorum

---

## 📚 GÜNLÜK ÖĞRENME KAYNAKLARI

### Video Önerileri (günlük seçim)
- **Corey Schafer - Pandas Tutorials** (YouTube)
- **Data School - Pandas Q&A** (YouTube)
- **Kaggle Learn - Pandas Course** (Online)

### Pratik Kaynaklar
- **Kaggle Datasets** - Gerçek verilerle çalışma
- **Pandas Cheat Sheet** - Hızlı referans
- **Stack Overflow** - Problemleri çözme

### Günlük Notlar
Her gün şunları not al:
- [ ] Öğrendiğin 3 yeni kavram
- [ ] Karşılaştığın 1 zorluk ve çözümü
- [ ] Yarın tekrar etmek istediğin 1 konu

---

## ⚡ HIZLI İPUÇLARI

### Zaman Yönetimi
- **Pomodoro Tekniği**: 25 dk çalış, 5 dk ara
- **Sabah saatleri**: En zor konuları sabah çalış
- **Pratik öncelik**: Teori/pratik oranını 40/60 tut

### Öğrenme Teknikleri
- **Aktif not alma**: Kendi cümlelerinle özetler yaz
- **Hemen uygula**: Öğrendiğin her konuyu hemen kodla
- **Hata yap**: Hatalardan öğrenme en etkili yöntem
- **Tekrar et**: Önceki günlerin konularını hızlıca tekrar et

### Motivasyon
- **Günlük hedefe odaklan**: Büyük resmi düşünme, bugünü bitir
- **İlerlemeyi takip et**: Checkbox'ları işaretlemek motivasyon verir
- **Topluluk**: Discord/Slack gruplarına katıl
- **Sabır**: Öğrenme süreci, hemen mükemmel olmayı bekleme

---

## 🚀 GELECEK HAFTA HAZIRLIĞI

### 2. Hafta Önizleme (NumPy)
- [ ] NumPy'ın ne olduğunu araştır
- [ ] Pandas-NumPy ilişkisini merak et
- [ ] Temel matematiksel kavramları hatırla
- [ ] Linear algebra terimlerini gözden geçir

### Pekiştirme
Bu hafta sonu:
- [ ] En zorlandığın konuları tekrar et
- [ ] Proje dosyalarını düzenle
- [ ] GitHub repo oluşturmayı düşün
- [ ] CV'ne "Pandas" yetkinliği ekle

**Bu listeyi tamamladığında Pandas'ın %80'ini öğrenmiş olacaksın! 🎉**