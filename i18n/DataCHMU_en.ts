<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="en_US" sourcelanguage="cs_CZ">
<context>
    <name>DataCHMU</name>
    <message>
        <location filename="../data_chmu.py" line="141"/>
        <source>&amp;ČHMÚ - data o počasí</source>
        <translation>&amp;CHMI - meteorological data processing</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="128"/>
        <source>Prostorová data o počasí</source>
        <translation>Spatial meteorological data</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="204"/>
        <source>Chyba: Pro správné fungování nástroje zapněte &apos;Processing&apos; plugin.</source>
        <translation>Error: To ensure proper functioning of the tool, enable the &apos;Processing&apos; plugin.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="212"/>
        <source>Chyba: V sekci Nastavení zadejte platnou absolutní cestu vstupních dat.</source>
        <translation>Error: In the Settings section, enter a valid absolute path for the input data.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="215"/>
        <source>Chyba: V adresáři vstupních dat chybí jedna z kategorií.</source>
        <translation>Error: One of the categories is missing in the input data directory.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="221"/>
        <source>Chyba: Zadaná adresářová cesta nesměřuje do složky &apos;spatial_data&apos;.</source>
        <translation>Error: The specified directory path does not point to the &apos;spatial_data&apos; folder.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="229"/>
        <source>Chyba vstupních parametrů: Zadejte vrstvu pro rozsah výstupu.</source>
        <translation>Input parameter error: Please enter a layer for the output extent.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="256"/>
        <source>Chyba vstupních parametrů: Počáteční datum je až po koncovém datumu.</source>
        <translation>Input parameter error: The start date is after the end date.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="259"/>
        <source>Chyba vstupních parametrů: Počáteční a koncové datum nemůže být stejné.</source>
        <translation>Input parameter error: The start date and end date cannot be the same.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="298"/>
        <source>Hotovo: Tedy doufám :)).</source>
        <translation>Done: Well, I hope so :)).</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="301"/>
        <source>Chyba: Ve Vaší oblasti se nenachází žádné měřící stanice - oblast přesuňte či zvětšte.</source>
        <translation>Error: No measuring stations are located in your area - move or zoom out on the area.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="304"/>
        <source>Chyba: Z Vámi zadaného časového období nelze vytvořit rastr.</source>
        <translation>Error: A raster cannot be created from the specified time period.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="307"/>
        <source>Chyba: Vzniklá bodová pole se nepovedlo nahrát.</source>
        <translation>Error: The resulting point fields could not be loaded.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="218"/>
        <source>Chyba: V jedné z kategorií vstupních dat chybí bodová vrstva měřících stanic.</source>
        <translation>Error: The point layer of the measuring stations is missing in one of the input data categories.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="310"/>
        <source>Chyba: Vámi zadanou vstupního vrstvu se nepodařilo načíst.</source>
        <translation>The input layer you provided could not be loaded.</translation>
    </message>
    <message>
        <location filename="../data_chmu.py" line="240"/>
        <source>Chyba vstupních parametrů: Pro volbu rozsahu zadejte vektorovou vrtvu.</source>
        <translation>Input parameter error: Please provide a vector layer for the extent selection.</translation>
    </message>
</context>
<context>
    <name>DataCHMUDialogBase</name>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="46"/>
        <source>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Výstup:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Output:&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="63"/>
        <source>Rastr</source>
        <translation>Raster</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="105"/>
        <source>Hlavní parametry</source>
        <translation>Primary parameters:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="186"/>
        <source>Kategorie:</source>
        <translation>Category:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="193"/>
        <source>Rozsah dle vrstvy:</source>
        <translation>Layer extent:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="211"/>
        <source>Do:</source>
        <translation>End:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="246"/>
        <source>Od:</source>
        <translation>Start:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="296"/>
        <source>Vedlejší parametry</source>
        <translation>Secondary parameters:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="304"/>
        <source>Velikost buňky:</source>
        <translation>Cell size:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="314"/>
        <source>Export bodových polí:</source>
        <translation>Point layers export:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="327"/>
        <source>Nearest Neighbour</source>
        <translation>Nearest Neighbour</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="351"/>
        <source>Cesta:</source>
        <translation>Path:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="384"/>
        <source>Ne</source>
        <translation>No</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="394"/>
        <source>Ano</source>
        <translation>Yes</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="406"/>
        <source>Interpolační metoda:</source>
        <translation>Interpolation method:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="413"/>
        <source>Projekce:</source>
        <translation>Projection:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="430"/>
        <source>Uložení:</source>
        <translation>Saving:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="457"/>
        <source>Virtuální vrstva</source>
        <translation>Virtual layer</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="467"/>
        <source>Soubor</source>
        <translation>File</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="488"/>
        <source>Koeficient vzdálenosti P:</source>
        <translation>Distance coefficient P:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="533"/>
        <source>Nearest Neighbour nevyžaduje žádné dodatečné parametry.</source>
        <translation>Nearest Neighbour does not require any additional parameters.</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="574"/>
        <source>Nastavení</source>
        <translation>Settings</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="669"/>
        <source>Cesta dekomprimovaného adresáře:</source>
        <translation>Path of the decompressed directory:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="640"/>
        <source>Google Disk</source>
        <translation>Google Disk</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="703"/>
        <source>Odkaz ke stažení dat:</source>
        <translation>Link to download data:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="836"/>
        <source>Start</source>
        <translation>Run</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="846"/>
        <source>Nápověda</source>
        <translation>Help</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="615"/>
        <source>Odkaz ke stažení skriptů:</source>
        <translation>Link to download scripts:</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="38"/>
        <source>ČHMÚ – zpracování meteorologických dat</source>
        <translation>CHMI – Meteorological Data Processing</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="123"/>
        <source>Průměrná denní teplota vzduchu</source>
        <translation>Average daily air temperature</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="128"/>
        <source>Maximální denní teplota vzduchu</source>
        <translation>Maximum daily air temperature</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="133"/>
        <source>Minimální denní teplota vzduchu</source>
        <translation>Minimum daily air temperature</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="138"/>
        <source>Průměrná denní relativní vlhkost vzduchu</source>
        <translation>Average daily relative humidity</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="143"/>
        <source>Denní úhrn srážek</source>
        <translation>Daily precipitation total</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="148"/>
        <source>Výška nově napadlého sněhu</source>
        <translation>Height of newly fallen snow</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="153"/>
        <source>Celková výška sněhové pokrývky</source>
        <translation>Total snow cover depth</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="158"/>
        <source>Denní úhrn doby trvání slunečního svitu</source>
        <translation>Daily total duration of sunshine</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="163"/>
        <source>Průměrný denní tlak vzduchu</source>
        <translation>Average daily air pressure</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="168"/>
        <source>Průměrná denní rychlost větru</source>
        <translation>Average daily wind speed</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="173"/>
        <source>Maximální rychlost větru</source>
        <translation>Maximum wind speed</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="178"/>
        <source>Globální záření</source>
        <translation>Global radiation</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="322"/>
        <source>IDW</source>
        <translation>IDW</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="681"/>
        <source>  GitHub  </source>
        <translation>GitHub</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="771"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;MS Shell Dlg 2&apos;; font-size:8pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Prosím čekejte...&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;MS Shell Dlg 2&apos;; font-size:8pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;Please wait...&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
    <message>
        <location filename="../data_chmu_dialog_base.ui" line="812"/>
        <source>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;MS Shell Dlg 2&apos;; font-size:8pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-weight:600;&quot;&gt;O pluginu&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Tento plugin umožňuje zpracování meteorologických měření ČHMÚ pomocí metod prostorové interpolace. Pro správnou funkčnost vyžaduje specificky upravené soubory, které lze stáhnout v sekci &lt;span style=&quot; font-weight:600;&quot;&gt;Nastavení&lt;/span&gt;. Zde je také dostupný odkaz ke stažení skriptů pro automatické stahování původních souborů z webu ČHMÚ a jejich následnou konverzi do formátu vhodného pro zpracování v GIS.&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Absolutní cestu k adresáři &lt;span style=&quot; font-weight:600;&quot;&gt;&amp;quot;spatial_data&amp;quot;&lt;/span&gt;, který si buď stáhnete a dekomprimujete, nebo vytvoříte pomocí zveřejněných skriptů, je nutné zadat do příslušného pole v sekci Nastavení. Pro správné fungování pluginu &lt;span style=&quot; font-weight:600;&quot;&gt;nesmí&lt;/span&gt; být změněna struktura adresáře ani upravovány poskytované soubory!&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Vstupní vrstva musí být &lt;span style=&quot; font-weight:600;&quot;&gt;vektorová&lt;/span&gt;, ideálně polygonová, a nahraná v aktuálním projektu.&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;Pro více informací stiskněte tlačítko &lt;span style=&quot; font-weight:600;&quot;&gt;Nápověda&lt;/span&gt;.&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</source>
        <translation>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:&apos;MS Shell Dlg 2&apos;; font-size:8.25pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:8pt; font-weight:600;&quot;&gt;About the plugin&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt;This plugin allows the processing of weather measurements from the Czech Hydrometeorological Institute (CHMI) using spatial interpolation methods. For proper functionality, it requires specifically formatted files, which can be downloaded in the &lt;/span&gt;&lt;span style=&quot; font-size:8pt; font-weight:600;&quot;&gt;Settings&lt;/span&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt; section. A link to download scripts for automatic downloading of the original files from the CHMI website and their subsequent conversion to a format suitable for GIS processing is also available here.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt;The absolute path to the directory &lt;/span&gt;&lt;span style=&quot; font-size:8pt; font-weight:600;&quot;&gt;&amp;quot;spatial_data&amp;quot;&lt;/span&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt;, which you either download and decompress, or create using the published scripts, must be entered in the relevant field in the Settings section. For the plugin to function correctly, the directory structure &lt;/span&gt;&lt;span style=&quot; font-size:8pt; font-weight:600;&quot;&gt;must not&lt;/span&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt; be altered, nor should the provided files be modified!&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt;The input layer of the extent must be &lt;/span&gt;&lt;span style=&quot; font-size:8pt; font-weight:600;&quot;&gt;vector&lt;/span&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt;, ideally a polygon, and loaded in the current project.&lt;/span&gt;&lt;/p&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;&quot;&gt;&lt;br /&gt;&lt;/p&gt;
&lt;p style=&quot; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt;For more information, press the &lt;/span&gt;&lt;span style=&quot; font-size:8pt; font-weight:600;&quot;&gt;Help&lt;/span&gt;&lt;span style=&quot; font-size:8pt;&quot;&gt; button.&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</translation>
    </message>
</context>
</TS>
