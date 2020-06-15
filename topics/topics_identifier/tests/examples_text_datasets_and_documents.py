from topics_identifier.models import Cluster, Document

cluster0 = {
    "terms" : "['currar', 'ir', 'guardo', '310']",
    "reference_doc": "#310 No. Las guardo para cuando tenga que ir a currar.",
    "documents": ['#4 Cuéntame tu,  a mi no me consta.', '!Brutal! {lol}', '#310 No. Las guardo para cuando tenga que ir a currar.', 'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA']
}

cluster1 = {
    "terms" : "['elegantemente', 'melón', 'abrir', 'forma', 'evidente', 'peor', 'niegan', 'si', '21']",
    "reference_doc": "#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...",
    "documents": ['#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...']
}

cluster2 = {
    "terms" : "['chalao', 'dices', 'anticuerpos', 'transpasar', '355']",
    "reference_doc": "#355 Transpasar anticuerpos? Que dices chalao...",
    "documents": ['basta jugar fallout para darse cuenta', '#355 Transpasar anticuerpos? Que dices chalao...']
}

cluster3 = {
    "terms" : "['precios', 'suban', 'privadas', 'empresas', 'explícale', '13', 'hace']",
    "reference_doc": "#13 explícale que es la que hace que las empresas privadas no suban precios",
    "documents": ['Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.', '#23 Pujol ya era expresidente antes que Torra llegara y le retiraron la pensión (injustamente)  hace unos años. No te enteras de nada. \n\n\nQuien sí la cobra es Montilla que es el origen de todos los problemas aunque no lo sepas porque no sabes nada anterior a 2010 (y de después la mitad). \n\n\nY también cobran los expresidentes de todas esas regiones  deficitarias e improductivas que tanto os gustan.\n\n\nPor cierto  , para sueldo subido el de Colau, ¿era el 40%?', '#13 explícale que es la que hace que las empresas privadas no suban precios']
}

test_dataset = {
    "name": "test_comments10",
    "description": "Test dataset with 10 documents",
    "terms": "['13', '2010', '21', '23', '310', '355', '40', '8kbxfauvdxa', 'abrir', 'ahora', 'alarma', 'allá', 'anterior', 'anticuerpos', 'aunque', 'años', 'basta', 'be', 'boe', 'brutal', 'chalao', 'cierto', 'cobra', 'cobran', 'colau', 'consta', 'cuenta', 'currar', 'cuéntame', 'darse', 'deficitarias', 'después', 'dices', 'elegantemente', 'empresas', 'enteras', 'evidente', 'explícale', 'expresidente', 'expresidentes', 'fallout', 'falta', 'forma', 'full', 'gatos', 'guardo', 'gustan', 'hace', 'https', 'improductivas', 'injustamente', 'ir', 'jugar', 'ley', 'llegara', 'lol', 'melón', 'mismo', 'mitad', 'montilla', 'niegan', 'origen', 'pantomima', 'parlamento', 'penalice', 'pensión', 'peor', 'precios', 'privadas', 'problemas', 'prohíba', 'publicaciones', 'pujol', 'regiones', 'retiraron', 'sabes', 'sacado', 'sepas', 'si', 'suban', 'subido', 'sueldo', 'todas', 'torra', 'transpasar', 'youtu']",
    "documents": [
        '#4 Cuéntame tu,  a mi no me consta.',
        '!Brutal! {lol}',
         'Pero más allá del estado de alarma y sus publicaciones en el BOE, ¿qué ley han sacado ahora mismo que penalice o prohíba algo de esto?\n\nQue para eso hace falta el parlamento.',
         '#310 No. Las guardo para cuando tenga que ir a currar.',
         '#23 Pujol ya era expresidente antes que Torra llegara y le retiraron la pensión (injustamente)  hace unos años. No te enteras de nada. \n\n\nQuien sí la cobra es Montilla que es el origen de todos los problemas aunque no lo sepas porque no sabes nada anterior a 2010 (y de después la mitad). \n\n\nY también cobran los expresidentes de todas esas regiones  deficitarias e improductivas que tanto os gustan.\n\n\nPor cierto  , para sueldo subido el de Colau, ¿era el 40%?',
         'basta jugar fallout para darse cuenta',
         '#21 si lo niegan es peor porque es evidente. Esto es una forma de abrir un melón elegantemente...',
         '#355 Transpasar anticuerpos? Que dices chalao...',
         'Pantomima Full - Gatos.\nhttps://youtu.be/8kbXfAuvdxA',
         '#13 explícale que es la que hace que las empresas privadas no suban precios'],
    "predicted_clusters": [0, 0, 3, 0, 3, 2, 1, 2, 0, 3],
    "clusters": [ cluster0, cluster1, cluster2, cluster3 ],
    "filenames": [   'data/texts/comments/comments_sample_small_2.txt',
                     'data/texts/comments/comments_sample_small_8.txt',
                     'data/texts/comments/comments_sample_small_4.txt',
                     'data/texts/comments/comments_sample_small_9.txt',
                     'data/texts/comments/comments_sample_small_10.txt',
                     'data/texts/comments/comments_sample_small_6.txt',
                     'data/texts/comments/comments_sample_small_7.txt',
                     'data/texts/comments/comments_sample_small_3.txt',
                     'data/texts/comments/comments_sample_small_1.txt',
                     'data/texts/comments/comments_sample_small_5.txt']
}

example_documents_short = [
    "Bla bla bla", "Ble ble ble", "Bli bli bli"
]

example_documents_long = [
    '''Explicando el famoso paper: "Proyectando la dinámica de transmisión del SARS-CoV-2" <p>Hace ya unos d&iacute;as, la revista&nbsp;<strong>Science</strong>&nbsp;public&oacute; uno de los&nbsp;<em>papers</em>&nbsp;m&aacute;s importantes de la historia reciente. Es un trabajo desarrollado por investigadores de Harvard&nbsp;y se titula:&nbsp;<strong>"Proyectando la din&aacute;mica de transmisi&oacute;n del SARS-CoV-2 durante el per&iacute;odo pospand&eacute;mico"</strong>. Ten&eacute;is el original&nbsp;<a href="https://science.sciencemag.org/content/early/2020/04/24/science.abb5793">aqu&iacute;</a>, y una traducci&oacute;n al castellano que yo mismo realic&eacute; en este mismo blog&nbsp;<a href="http://quevidaesta2010.blogspot.com/2020/04/proyectando-la-dinamica-de-transmision.html">aqu&iacute;</a>.</p><p>El trabajo de estos autores de los departamentos de&nbsp;<strong>Inmunolog&iacute;a y Enfermedades Infecciosas e&nbsp;Epidemiolog&iacute;a</strong>&nbsp;de Harvard es a la vez simple y complejo de entender. Es complejo en cuanto a la metodolog&iacute;a estad&iacute;stica y los modelos matem&aacute;ticos utilizados (detalles al alcance de los m&aacute;s expertos en la materia que se recogen en un apartado de&nbsp;<a href="https://science.sciencemag.org/cgi/content/full/science.abb5793/DC1">materiales complementarios</a>&nbsp;que ya de por s&iacute; es casi un&nbsp;<em>paper</em>&nbsp;independiente por lo denso). Pero a la vez es simple en cuanto a lo "sencillo" que es entender los resultados de la aplicaci&oacute;n de dichos modelos frente al mundo real.</p><p>Voy a intentar ser breve en esta entrada para que todos entendamos los posibles escenarios que los expertos barajan en estos momentos para el periodo pand&eacute;mico y el futuro&nbsp;pospand&eacute;mico. Es decir, para la din&aacute;mica del virus: &iquest;qu&eacute; es probable que ocurra con el&nbsp;<strong>SARS-CoV-2</strong>&nbsp;en los pr&oacute;ximos meses y a&ntilde;os?</p><h3><strong>Comentarios iniciales.</strong></h3><p>Es necesario comentar antes de nada un par de cuestiones imprescindibles para poder entender m&iacute;nimamente la din&aacute;mica del&nbsp;<strong>SARS-CoV-2</strong>:</p><p>1) El&nbsp;<strong>COVID-19</strong>&nbsp;es el nombre que se le ha dado a la enfermedad que causa el virus denominado&nbsp;<strong>SARS-CoV-2.&nbsp;</strong>Una cosa es la enfermedad (como por ejemplo, el SIDA), y otra el virus que lo causa (en el caso del SIDA es el VIH).</p><p>2) El virus&nbsp;<strong>SARS-CoV-2&nbsp;</strong>es un&nbsp;<strong>coronavirus</strong>&nbsp;(<em>Orthocoronavirinae</em>). Para la subfamilia del&nbsp;<strong>coronavirus</strong>&nbsp;existen a su vez cuatro g&eacute;neros: Alphacoronavirus, Betacoronavirus, Gammacoronavirus y Deltacoronavirus. El&nbsp;<strong>SARS-CoV-2</strong>&nbsp;pertenece al g&eacute;nero&nbsp;<em>Betacoronavirus</em>.</p><p>3) Adem&aacute;s del&nbsp;<strong>SARS-CoV-2</strong>, existen muchos otros virus de la subfamilia&nbsp;<strong>coronavirus</strong>&nbsp;que son capaces de transmitirse de humano a humano. Entre ellos tenemos al&nbsp;<strong>MERS-CoV</strong>&nbsp;(que produce desde el 2015 la enfermedad a&uacute;n en activo llamada:&nbsp;s&iacute;ndrome respiratorio de Oriente Medio), el&nbsp;<strong>SARS-CoV-1</strong>&nbsp;(que apareci&oacute; y desapareci&oacute; entre los a&ntilde;os 2002/2003 produciendo la enfermedad:&nbsp;s&iacute;ndrome respiratorio agudo grave), y otros muchos virus que por su levedad cuadran y se aglutinan en lo que se llama&nbsp;<strong>resfriado com&uacute;n</strong>. Es decir, que eso que nos contagia casi cada a&ntilde;o y que denominamos&nbsp;<strong>resfriado</strong>&nbsp;(enfermedad), es en realidad producto casi siempre de un tipo de los restantes&nbsp;<strong>coronavirus</strong>&nbsp;capaces de infectar humanos.</p><p>4) El 15% de los resfriados son causados por coronavirus, y de estos casos, la mayor parte los producen los coronavirus:&nbsp;<strong>HCoV-229E, HCoV-NL63, HCoV-0C43 y HCoV-HKU1.</strong></p><p>5) De entre estos cuatro, s&oacute;lo dos pertenecen al mismo g&eacute;nero&nbsp;<em>Betacoronavirus&nbsp;</em>del<em>&nbsp;</em><strong>SARS-CoV-1</strong>,&nbsp;<strong>SARS-CoV-2</strong>, y el&nbsp;<strong>MERS-CoV</strong>. Se trata del&nbsp;<strong>HCoV-OC43 y el HCoV-HKU1.</strong></p><p>6) Todos los&nbsp;<em>Betacoronavirus&nbsp;</em>presentan, dada su similitud filogen&eacute;tica, cierta inmunidad cruzada. Se conoce la realidad este proceso gracias al estudio de los coronavirus del resfriado com&uacute;n. Por ejemplo; pasar el&nbsp;<strong>HCoV-OC43</strong>&nbsp;te inmuniza hasta cierto punto y tiempo frente al&nbsp;<strong>HCoV-HKU1</strong>, y viceversa. En el estudio del que estamos hablando se supone, seg&uacute;n el escenario, que tambi&eacute;n existe cierta inmunidad cruzada entre estos virus "del resfriado" y el&nbsp;<strong>SARS-CoV-2</strong>. Y modelan la din&aacute;mica del COVID19 otorgando varios valores a dicho factor de inmunidad cruzada (de m&aacute;s d&eacute;bil a m&aacute;s fuerte).</p><p>7) Por otra parte, el estudio tambi&eacute;n basa los escenarios pronosticados a partir de lo que denominan&nbsp;<strong>factor estacional</strong>. Es decir, cu&aacute;nto y c&oacute;mo afecta al virus los climas h&uacute;medos y las temperaturas m&aacute;s altas. En este sentido, var&iacute;an tambi&eacute;n en las simulaciones que realizan los n&uacute;meros para este factor.</p><p>8) Tambi&eacute;n utilizan, por supuesto, el factor m&aacute;s importante para todo modelo epidemiol&oacute;gico: la inmunidad de grupo. Es decir, cu&aacute;ndo y c&oacute;mo se alcanzar&aacute; el punto en que m&aacute;s del 60% de la poblaci&oacute;n deja de ser susceptible al virus (por haber pasado la enfermedad). En este sentido, cobra especial importancia para entender la din&aacute;mica futura conocer cu&aacute;nta inmunidad (anticuerpos) produce nuestro cuerpo tras pasar la infecci&oacute;n, y qu&eacute; "memoria" o duraci&oacute;n tienen dichos anticuerpos. En este sentido, y a ra&iacute;z de lo que se sabe de los virus del resfriado&nbsp;<strong>HCoV-OC43 y HCoV-HKU1</strong>, proponen que la inmunidad dura entre 40 semanas (en el peor escenario) y 104 semanas (en el mejor caso). La&nbsp;<strong>inmunidad permanente</strong>&nbsp;la tienen en cuenta, pero se sabe que es un escenario MUY poco probable.</p><p>9) Finalmente, toman como par&aacute;metro para la simulaci&oacute;n&nbsp;<strong>la intensidad y el momento de las medidas de control que tomen los gobiernos (aunque este punto lo retomaremos en futuras entradas del blog).</strong></p><h3><strong>Simulando la transmisi&oacute;n de SARS-CoV-2.</strong></h3><p>En el&nbsp;<em>paper</em>&nbsp;el equipo de investigaci&oacute;n explica que han utilizado el modelo epidemiol&oacute;gico de transmisi&oacute;n&nbsp;<strong>SEIRS</strong>&nbsp;y que lo han ajustado a partir de todos los datos disponibles para los&nbsp;<em>Betacoronavirus</em>&nbsp;<strong>HCoV-OC43 y HCoV-HKU1</strong>&nbsp;que, como hemos dicho, son muy cercanos filogen&eacute;ticamente al&nbsp;<strong>SARS-CoV-2</strong>. Para justificar el buen ajuste de este modelo muestran las primeras dos figuras (Fig.1 y Fig.2) que no nos interesan demasiado para lo que trataremos aqu&iacute;. Demos por bueno el modelo y veamos que nos dice:</p><p>La primera gr&aacute;fica de inter&eacute;s es la que denominan&nbsp;<strong>Fig. 3</strong>&nbsp;"Distintos escenarios de prevalencia para el SARS-CoV-2 en regiones templadas durante los pr&oacute;ximos cinco a&ntilde;os". Se trata de la siguiente figura:</p><p><a href="https://1.bp.blogspot.com/-EGyu_N5N1eY/XpgTsR8Cx0I/AAAAAAAAC5U/ZvVHEU-u2-k_vW5cQQKiumVtkGSw1PvUACPcBGAYYCw/s1600/F3.large.jpg"><img src="https://1.bp.blogspot.com/-EGyu_N5N1eY/XpgTsR8Cx0I/AAAAAAAAC5U/ZvVHEU-u2-k_vW5cQQKiumVtkGSw1PvUACPcBGAYYCw/s640/F3.large.jpg"></a></p><p>Los picos rojos y azules son para los&nbsp;<em>Betacoronavirus</em>&nbsp;del resfriado com&uacute;n, mientras que los picos en negros son los del&nbsp;<strong>SARS-CoV-2</strong>. En el eje X tenemos los a&ntilde;os por venir (se ve una l&iacute;nea vertical en negro indicando donde estamos ahora: abril del 2020). En el eje Y tenemos&nbsp;<em>grosso modo</em>&nbsp;la cantidad de infectados por cada 1000 habitantes: por ponerlo en claro, cu&aacute;nto m&aacute;s alto el pico m&aacute;s cantidad de infectados en general. Si el pico llega cerca del 100, eso indicar&iacute;a que una gran parte de toda la poblaci&oacute;n mundial estar&iacute;a infectada en ese momento.</p><h3><strong>Fij&eacute;monos en el escenario A).</strong></h3><p><a href="https://1.bp.blogspot.com/-qtK2ECDOTVA/XqQJajQEfJI/AAAAAAAAC6s/N289Uvu9iSQmlfToIi2zbyt07S__rcNAwCLcBGAsYHQ/s1600/casoA.png"><img src="https://1.bp.blogspot.com/-qtK2ECDOTVA/XqQJajQEfJI/AAAAAAAAC6s/N289Uvu9iSQmlfToIi2zbyt07S__rcNAwCLcBGAsYHQ/s640/casoA.png"></a></p><p>Esta gr&aacute;fica en concreto se basa en los siguientes valores para los par&aacute;metros m&aacute;s importantes del modelo:&nbsp;(A) &chi; 3X = 0.3, &chi; X3 = 0, 1 / &sigma; 3 = 40 semanas, f = 0.2.</p><p>- &chi; 3X = 0.3, &chi; X3 = 0, indica que en este escenario hay muy poca inmunidad cruzada entre los&nbsp;<em>Betacoronavirus</em>&nbsp;del resfriado com&uacute;n y el&nbsp;<strong>SARS-CoV-2</strong>.<strong>&nbsp;</strong>Es decir, que&nbsp;<strong>pillar un resfriado no implicar&iacute;a tener mucha menos probabilidad de pillar COVID19.</strong></p><p>- 1 / &sigma; 3 = 40, implica una&nbsp;<strong>corta duraci&oacute;n (40 semanas) de inmunidad</strong>&nbsp;contra el&nbsp;<strong>SARS-CoV-2</strong>&nbsp;una vez pasada la enfermedad: es decir, los anticuerpos generados no nos otorgan mucha protecci&oacute;n conforme pasan los meses. Obviamente no se estima inmunidad permanente para este escenario.</p><p>-&nbsp;f = 0.2, implica poca variaci&oacute;n estacional. En este caso, el&nbsp;<strong>SARS-CoV-2&nbsp;</strong>se ver&iacute;a relativamente&nbsp;<strong>poco afectado</strong>&nbsp;por los cambios ambientales de humedad y temperatura.</p><p><strong>&iquest;Qu&eacute; significa pues este escenario A)?</strong></p><p>Que si la inmunidad cruzada con los coronavirus del resfriado com&uacute;n es baja, la inmunidad que nuestro cuerpo adquiere tras pasar la enfermedad no dura m&aacute;s de 40 semanas, y el factor ambiental (estacional) es poco importante;&nbsp;<strong>en caso de no poseerse vacunas, tratamientos, ni tomarse medidas de contenci&oacute;n</strong>, en la din&aacute;mica del virus ver&iacute;amos un gran pico en la primera pandemia (en la que estamos) y recurrentes brotes anuales que afectar&iacute;an a una parte muy importante de la poblaci&oacute;n: &iexcl;algo as&iacute; como 1 de cada 5 personas pasar&iacute;an el COVID19&nbsp;<strong>cada a&ntilde;o!</strong></p><h3><strong>Fij&eacute;monos en el&nbsp;escenario B).</strong></h3><p></p><p><a href="https://1.bp.blogspot.com/-yEomC_l1K_s/XqQKuxOnDpI/AAAAAAAAC64/xE2St8Pn3_I0QSVI2WYnSF0sSVe8scgAQCLcBGAsYHQ/s1600/casoB.png"><img src="https://1.bp.blogspot.com/-yEomC_l1K_s/XqQKuxOnDpI/AAAAAAAAC64/xE2St8Pn3_I0QSVI2WYnSF0sSVe8scgAQCLcBGAsYHQ/s640/casoB.png"></a></p><p>Esta gr&aacute;fica en concreto se basa en los siguientes valores para los par&aacute;metros m&aacute;s importantes del modelo:&nbsp;(B) &chi; 3X = 0.7, &chi; X3 = 0, 1 / &sigma; 3 = 104 semanas, f = 0.2.</p><p>- &chi; 3X = 0.7, &chi; X3 = 0, indica que en este escenario hay bastante inmunidad cruzada entre los&nbsp;<em>Betacoronavirus</em>&nbsp;del resfriado com&uacute;n y el&nbsp;<strong>SARS-CoV-2</strong>.<strong>&nbsp;</strong>Es decir, que&nbsp;<strong>pillar un resfriado&nbsp;</strong><strong>s&iacute;</strong><strong>&nbsp;implicar&iacute;a tener mucha menos probabilidad de pillar COVID19.</strong></p><p>- 1 / &sigma; 3 = 104, implica una&nbsp;"<strong>larga" duraci&oacute;n (104 semanas) de inmunidad</strong>&nbsp;contra el&nbsp;<strong>SARS-CoV-2</strong>&nbsp;una vez pasada la enfermedad: es decir, los anticuerpos generados nos otorgan bastante protecci&oacute;n conforme pasan los meses.&nbsp;<strong>Pero tampoco se trata de inmunidad permanente.</strong></p><p>-&nbsp;f = 0.2, implica poca variaci&oacute;n estacional. En este caso, el&nbsp;<strong>SARS-CoV-2&nbsp;</strong>se ver&iacute;a relativamente&nbsp;<strong>poco afectado</strong>&nbsp;por los cambios ambientales de humedad y temperatura.</p><p><strong>&iquest;Qu&eacute; significa pues este escenario B)?</strong></p><p>Que si la inmunidad cruzada con los&nbsp;<strong>coronavirus</strong>&nbsp;del resfriado com&uacute;n es alta, la inmunidad que nuestro cuerpo adquiere tras pasar la enfermedad es duradera (alrededor de 104 semanas), y el factor ambiental (estacional) es poco importante;&nbsp;<strong>en caso de no poseerse vacunas, tratamientos, ni tomarse medidas de contenci&oacute;n</strong>, en la din&aacute;mica del virus&nbsp;ver&iacute;amos un gran pico en la primera pandemia (en la que estamos) y luego recurrentes brotes cada dos a&ntilde;os que afectar&iacute;an a una parte relativamente importante de la poblaci&oacute;n: &iexcl;algo as&iacute; como 1 de cada 6 personas pasar&iacute;an el COVID19&nbsp;<strong>cada dos a&ntilde;os!&nbsp;</strong>Entre estos dos a&ntilde;os de brotes relativamente importantes habr&iacute;an peque&ntilde;os brotes en los a&ntilde;os intermedios.</p><p><strong>Nota:&nbsp;</strong>Es interesante ver en esta gr&aacute;fica c&oacute;mo suponer una alta inmunidad cruzada hace que los casos de resfriado com&uacute;n tambi&eacute;n descender&iacute;an a nivel mundial debido al COVID19.</p><h3><strong>Fij&eacute;monos en el&nbsp;escenario C).</strong></h3><p><a href="https://1.bp.blogspot.com/-9VQiL8B8CTA/XqQM9pvDMZI/AAAAAAAAC7E/9WnCEFzTvCMOUL8d33tf-HA7sPZmWawSgCLcBGAsYHQ/s1600/CasoC.png"><img src="https://1.bp.blogspot.com/-9VQiL8B8CTA/XqQM9pvDMZI/AAAAAAAAC7E/9WnCEFzTvCMOUL8d33tf-HA7sPZmWawSgCLcBGAsYHQ/s640/CasoC.png"></a></p><p>Esta gr&aacute;fica en concreto se basa en los siguientes valores para los par&aacute;metros m&aacute;s importantes del modelo:&nbsp;(C) &chi; 3X = 0.7, &chi; X3 = 0, 1 / &sigma; 3= 104 semanas, f = 0.4.</p><p>- &chi; 3X = 0.7, &chi; X3 = 0, indica que en este escenario hay bastante inmunidad cruzada entre los&nbsp;<em>Betacoronavirus</em>&nbsp;del resfriado com&uacute;n y el&nbsp;<strong>SARS-CoV-2</strong>.<strong>&nbsp;</strong>Es decir, que&nbsp;<strong>pillar un resfriado&nbsp;</strong><strong>s&iacute;</strong><strong>&nbsp;implicar&iacute;a tener mucha menos probabilidad de pillar COVID19.</strong></p><p>- 1 / &sigma; 3 = 104, implica una&nbsp;"<strong>larga" duraci&oacute;n (104 semanas) de inmunidad</strong>&nbsp;contra el&nbsp;<strong>SARS-CoV-2</strong>&nbsp;una vez pasada la enfermedad: es decir, los anticuerpos generados nos otorgan bastante protecci&oacute;n conforme pasan los meses.&nbsp;<strong>Pero tampoco se trata de inmunidad permanente.</strong></p><p>-&nbsp;f = 0.4, implica&nbsp;<strong>alta variaci&oacute;n estacional</strong>. En este caso, el&nbsp;<strong>SARS-CoV-2&nbsp;</strong>se ver&iacute;a&nbsp;<strong>bastante&nbsp;afectado</strong>&nbsp;por los cambios ambientales de humedad y temperatura. Esta es la &uacute;nica variable que se modifica con respecto al escenario B).</p><p><strong>&iquest;Qu&eacute; significa pues este escenario C)?</strong></p><p>Que si la inmunidad cruzada con los&nbsp;<strong>coronavirus</strong>&nbsp;del resfriado com&uacute;n es alta, la inmunidad que nuestro cuerpo adquiere tras pasar la enfermedad es duradera (alrededor de 104 semanas), y el factor ambiental (estacional) es&nbsp;<strong>bastante</strong>&nbsp;importante;&nbsp;<strong>en caso de no poseerse vacunas, tratamientos, ni tomarse medidas de contenci&oacute;n</strong>, en la din&aacute;mica del virus ver&iacute;amos como&nbsp;se reducir&iacute;a el tama&ntilde;o m&aacute;ximo de la onda de infecci&oacute;n inicial, pero que se llegar&iacute;an a producir brotes en invierno mucho m&aacute;s severos a partir de ese momento [<strong>comp&aacute;rese con (B)</strong>].</p><p><strong>Nota:&nbsp;&iexcl;</strong>Se puede observar que, contrariamente a lo que muchos creen, el hecho de que el factor ambiental sea importante podr&iacute;a llevar a escenarios mucho m&aacute;s severos que en el caso donde los cambios estacionales no son relevantes!</p><h3><strong>Fij&eacute;monos en el&nbsp;escenario D).</strong></h3><p><a href="https://1.bp.blogspot.com/-ZxTGGv5IMp8/XqQOroN9KSI/AAAAAAAAC7Q/jBRLlh6lGnkKlwtLiissq8ehi1v6y7u3ACLcBGAsYHQ/s1600/CasoD.png"><img src="https://1.bp.blogspot.com/-ZxTGGv5IMp8/XqQOroN9KSI/AAAAAAAAC7Q/jBRLlh6lGnkKlwtLiissq8ehi1v6y7u3ACLcBGAsYHQ/s640/CasoD.png"></a></p><p>Esta gr&aacute;fica en concreto se basa en los siguientes valores para los par&aacute;metros m&aacute;s importantes del modelo:&nbsp;(D) &chi; 3X = 0.7, &chi; X3 = 0, 1 / &sigma; 3 = infinito, f = 0.2.</p><p>- &chi; 3X = 0.7, &chi; X3 = 0, indica que en este escenario hay bastante inmunidad cruzada entre los&nbsp;<em>Betacoronavirus</em>&nbsp;del resfriado com&uacute;n y el&nbsp;<strong>SARS-CoV-2</strong>.<strong>&nbsp;</strong>Es decir, que&nbsp;<strong>pillar un resfriado&nbsp;</strong><strong>s&iacute;</strong><strong>&nbsp;implicar&iacute;a tener mucha menos probabilidad de pillar COVID19.</strong></p><p>- 1 / &sigma; 3 = infinito, implica que la&nbsp;<strong>inmunidad&nbsp;es permanente.&nbsp;</strong>Una vez pasas el COVID19 los anticuerpos de tu cuerpo impiden que jam&aacute;s vuelvas a pasar la enfermedad.</p><p>-&nbsp;f = 0.2, implica poca variaci&oacute;n estacional. En este caso, el&nbsp;<strong>SARS-CoV-2&nbsp;</strong>se ver&iacute;a relativamente&nbsp;<strong>poco afectado</strong>&nbsp;por los cambios ambientales de humedad y temperatura.</p><p><strong>&iquest;Qu&eacute; significa pues este escenario D)?</strong></p><p>Que si la inmunidad cruzada con los&nbsp;<strong>coronavirus</strong>&nbsp;del resfriado com&uacute;n es alta, la inmunidad que nuestro cuerpo adquiere tras pasar la enfermedad es permanente (infinita en el tiempo), y el factor ambiental (estacional) es&nbsp;<strong>poco</strong>&nbsp;importante;&nbsp;<strong>en caso de no poseerse vacunas, tratamientos, ni tomarse medidas de contenci&oacute;n</strong>, en la din&aacute;mica del virus ver&iacute;amos que la inmunidad de grupo podr&iacute;a eliminar por completo al virus para siempre tras la infecci&oacute;n inicial en la que estamos.</p><p><strong>Nota:&nbsp;</strong>si este, poco probable, escenario fuese el bueno, es interesante notar como de camino acabar&iacute;amos con las dos cepas de&nbsp;<em>Betacoronavirus</em>&nbsp;que nos causan resfriado com&uacute;n (l&iacute;neas rojas y azul). &iexcl;El&nbsp;<strong>HCoV-OC43 y el HCoV-HKU1</strong>&nbsp;tambi&eacute;n ser&iacute;an erradicados!</p><h3><strong>Fij&eacute;monos en el&nbsp;escenario E).</strong></h3><p><a href="https://1.bp.blogspot.com/-8ivoSGMQzx4/XqQQauireiI/AAAAAAAAC7c/F6Q5F-bpZCgxZhOSg7JCl6bl04mYZAsqACLcBGAsYHQ/s1600/casoE.png"><img src="https://1.bp.blogspot.com/-8ivoSGMQzx4/XqQQauireiI/AAAAAAAAC7c/F6Q5F-bpZCgxZhOSg7JCl6bl04mYZAsqACLcBGAsYHQ/s640/casoE.png"></a></p><p>Esta gr&aacute;fica en concreto se basa en los siguientes valores para los par&aacute;metros m&aacute;s importantes del modelo:&nbsp;(E) &chi; 3X = 0.3, &chi; X3 = 0.3, 1 / &sigma; 3 = 104 semanas, f = 0.4.</p><p>- &chi; 3X = 0.3, &chi; X3 = 0, indica que en este escenario hay muy poca inmunidad cruzada entre los&nbsp;<em>Betacoronavirus</em>&nbsp;del resfriado com&uacute;n y el&nbsp;<strong>SARS-CoV-2</strong>.<strong>&nbsp;</strong>Es decir, que&nbsp;<strong>pillar un resfriado no implicar&iacute;a tener mucha menos probabilidad de pillar COVID19.</strong></p><p>- 1 / &sigma; 3 = 104, implica una&nbsp;"<strong>larga" duraci&oacute;n (104 semanas) de inmunidad</strong>&nbsp;contra el&nbsp;<strong>SARS-CoV-2</strong>&nbsp;una vez pasada la enfermedad: es decir, los anticuerpos generados nos otorgan bastante protecci&oacute;n conforme pasan los meses.&nbsp;<strong>Pero tampoco es permanente.</strong></p><p>-&nbsp;f = 0.4, implica&nbsp;<strong>alta variaci&oacute;n estacional</strong>. En este caso, el&nbsp;<strong>SARS-CoV-2&nbsp;</strong>se ver&iacute;a&nbsp;<strong>bastante&nbsp;afectado</strong>&nbsp;por los cambios ambientales de humedad y temperatura.</p><p><strong>&iquest;Qu&eacute; significa pues este escenario E)?</strong></p><p>Que si la inmunidad cruzada con los&nbsp;<strong>coronavirus</strong>&nbsp;del resfriado com&uacute;n es baja, la inmunidad que nuestro cuerpo adquiere tras pasar la enfermedad es duradera (alrededor de 104 semanas), y el factor ambiental (estacional) es&nbsp;<strong>bastante</strong>&nbsp;importante;&nbsp;<strong>en caso de no poseerse vacunas, tratamientos, ni tomarse medidas de contenci&oacute;n</strong>, en la din&aacute;mica del virus ver&iacute;amos que&nbsp;un resurgimiento del&nbsp;<strong>SARS-CoV-2</strong>&nbsp;podr&iacute;a ocurrir tan tarde como en el 2024 despu&eacute;s de un per&iacute;odo de eliminaci&oacute;n&nbsp;<strong>aparente</strong>.</p><p><strong>Nota:&nbsp;</strong>es interesante notar como el hecho de que la inmunidad no sea permanente lleva a que incluso en las situaciones m&aacute;s desfavorables para el virus, &eacute;ste pueda resurgir tras varios picos y un periodo de varios a&ntilde;os donde falsamente parece que se logr&oacute; erradicar el virus, no siendo el caso ya que&nbsp;<strong>una vez la inmunidad de 104 semanas deja de tener efecto el virus reaparece con fuerza.</strong></p><h3><strong>Resumen:</strong></h3><p>-&nbsp;Si la inmunidad al&nbsp;<strong>SARS-CoV-2</strong>&nbsp;no es permanente, es muy probable que entre&nbsp;<strong>en circulaci&oacute;n regular.</strong></p><p>- La alta variaci&oacute;n estacional en la transmisi&oacute;n conduce a una menor incidencia m&aacute;xima durante la onda pand&eacute;mica inicial, pero a brotes recurrentes m&aacute;s severos en los sucesivos inviernos.</p><p>-&nbsp;Si la inmunidad al&nbsp;<strong>SARS-CoV-2</strong>&nbsp;es permanente, el virus podr&iacute;a desaparecer tras cinco a&ntilde;os o m&aacute;s despu&eacute;s de causar el actual brote.</p><p>-&nbsp;Unos bajos niveles de inmunidad cruzada frente a los otros&nbsp;<em>Betacoronavirus</em>&nbsp;(y sin inmunidad permanente) podr&iacute;an hacer que el&nbsp;<strong>SARS-CoV-2&nbsp;</strong>parezca extinguirse, solo para resurgir despu&eacute;s de unos a&ntilde;os.</p><p>- El&nbsp;<strong>SARS-CoV-2&nbsp;</strong>puede proliferar en cualquier &eacute;poca del a&ntilde;o. En todos los escenarios modelados el&nbsp;<strong>SARS-CoV-2</strong>&nbsp;fue capaz de producir un brote sustancial, independientemente del tiempo de establecimiento. Los establecimientos de invierno/primavera favorecieron los brotes con picos m&aacute;s bajos, mientras que los establecimientos de oto&ntilde;o/invierno condujeron a brotes m&aacute;s severos. Y cuanta m&aacute;s dependencia estacional exista, m&aacute;s severo y agudo ser&aacute; el brote anual (o bienal).</p><h3><strong>Pr&oacute;ximas entradas.</strong></h3><p>Para no hacer demasiado denso este art&iacute;culo, dejaremos para pr&oacute;ximas entradas del blog el estudio del abordaje que el equipo de Harvard hace sobre la evoluci&oacute;n (din&aacute;mica) del virus en el momento en que se toman medidas activas frente a la pandemia. Es decir, qu&eacute; posibles escenarios nos esperan para el virus seg&uacute;n sea la actitud tomada a partir de ahora por los gobiernos y la ciencia en general frente al COVID19.</p> '''

]

example_documents = {
    "short": example_documents_short,
    "long": example_documents_long,
}

stop_words_test = ['a', 'al', 'algo', 'algunas', 'algunos', 'ante', 'antes', 'como', 'con', 'contra', 'cual', 'cuando', 'de', 'del', 'desde', 'donde', 'durante', 'e', 'el', 'ella', 'ellas', 'ellos', 'en', 'entre', 'era', 'erais', 'eran', 'eras', 'eres', 'es', 'esa', 'esas', 'ese', 'eso', 'esos', 'esta', 'estaba', 'estabais', 'estaban', 'estabas', 'estad', 'estada', 'estadas', 'estado', 'estados', 'estamos', 'estando', 'estar', 'estaremos', 'estará', 'estarán', 'estarás', 'estaré', 'estaréis', 'estaría', 'estaríais', 'estaríamos', 'estarían', 'estarías', 'estas', 'este', 'estemos', 'esto', 'estos', 'estoy', 'estuve', 'estuviera', 'estuvierais', 'estuvieran', 'estuvieras', 'estuvieron', 'estuviese', 'estuvieseis', 'estuviesen', 'estuvieses', 'estuvimos', 'estuviste', 'estuvisteis', 'estuviéramos', 'estuviésemos', 'estuvo', 'está', 'estábamos', 'estáis', 'están', 'estás', 'esté', 'estéis', 'estén', 'estés', 'fue', 'fuera', 'fuerais', 'fueran', 'fueras', 'fueron', 'fuese', 'fueseis', 'fuesen', 'fueses', 'fui', 'fuimos', 'fuiste', 'fuisteis', 'fuéramos', 'fuésemos', 'ha', 'habida', 'habidas', 'habido', 'habidos', 'habiendo', 'habremos', 'habrá', 'habrán', 'habrás', 'habré', 'habréis', 'habría', 'habríais', 'habríamos', 'habrían', 'habrías', 'habéis', 'había', 'habíais', 'habíamos', 'habían', 'habías', 'han', 'has', 'hasta', 'hay', 'haya', 'hayamos', 'hayan', 'hayas', 'hayáis', 'he', 'hemos', 'hube', 'hubiera', 'hubierais', 'hubieran', 'hubieras', 'hubieron', 'hubiese', 'hubieseis', 'hubiesen', 'hubieses', 'hubimos', 'hubiste', 'hubisteis', 'hubiéramos', 'hubiésemos', 'hubo', 'la', 'las', 'le', 'les', 'lo', 'los', 'me', 'mi', 'mis', 'mucho', 'muchos', 'muy', 'más', 'mí', 'mía', 'mías', 'mío', 'míos', 'nada', 'ni', 'no', 'nos', 'nosotras', 'nosotros', 'nuestra', 'nuestras', 'nuestro', 'nuestros', 'o', 'os', 'otra', 'otras', 'otro', 'otros', 'para', 'pero', 'poco', 'por', 'porque', 'que', 'quien', 'quienes', 'qué', 'se', 'sea', 'seamos', 'sean', 'seas', 'seremos', 'será', 'serán', 'serás', 'seré', 'seréis', 'sería', 'seríais', 'seríamos', 'serían', 'serías', 'seáis', 'sido', 'siendo', 'sin', 'sobre', 'sois', 'somos', 'son', 'soy', 'su', 'sus', 'suya', 'suyas', 'suyo', 'suyos', 'sí', 'también', 'tanto', 'te', 'tendremos', 'tendrá', 'tendrán', 'tendrás', 'tendré', 'tendréis', 'tendría', 'tendríais', 'tendríamos', 'tendrían', 'tendrías', 'tened', 'tenemos', 'tenga', 'tengamos', 'tengan', 'tengas', 'tengo', 'tengáis', 'tenida', 'tenidas', 'tenido', 'tenidos', 'teniendo', 'tenéis', 'tenía', 'teníais', 'teníamos', 'tenían', 'tenías', 'ti', 'tiene', 'tienen', 'tienes', 'todo', 'todos', 'tu', 'tus', 'tuve', 'tuviera', 'tuvierais', 'tuvieran', 'tuvieras', 'tuvieron', 'tuviese', 'tuvieseis', 'tuviesen', 'tuvieses', 'tuvimos', 'tuviste', 'tuvisteis', 'tuviéramos', 'tuviésemos', 'tuvo', 'tuya', 'tuyas', 'tuyo', 'tuyos', 'tú', 'un', 'una', 'uno', 'unos', 'vosotras', 'vosotros', 'vuestra', 'vuestras', 'vuestro', 'vuestros', 'y', 'ya', 'yo', 'él', 'éramos', '']


def create_example_cluster(number=0, documents=False):
    terms = test_dataset["clusters"][number]["terms"]
    cluster = Cluster(dataset=test_dataset["name"], number=number, terms=terms)
    cluster.save()
    if documents:
        test_cluster = test_dataset["clusters"][number]
        for doc in test_cluster["documents"]:
            cluster.add_document(doc)
    return cluster

def create_example_document(type="short"):
    if type == "short":
        content = example_documents_short[0]
    else:
        content=example_documents_long[0]
    doc = Document(content=content)
    doc.save()
    return doc
