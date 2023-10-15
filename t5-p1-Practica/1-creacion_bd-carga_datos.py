from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:55017/')

db = client.ipc_database
ipc_data_2023 = db.ipc_data_2023


bulk_data = [
    {"Fecha": "2023-09-01T00:00:00.000+02:00", "T3_TipoDato": "Avance", "T3_Periodo": "M09", "Anyo": 2023, "Valor": 3.5}
    , {"Fecha": "2023-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2023,
       "Valor": 2.6}
    , {"Fecha": "2023-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2023,
       "Valor": 2.3}
    , {"Fecha": "2023-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2023,
       "Valor": 1.9}
    , {"Fecha": "2023-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2023,
       "Valor": 3.2}
    , {"Fecha": "2023-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2023,
       "Valor": 4.1}
    , {"Fecha": "2023-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2023,
       "Valor": 3.3}
    , {"Fecha": "2023-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2023,
       "Valor": 6.0}
    , {"Fecha": "2023-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2023,
       "Valor": 5.9}
    , {"Fecha": "2022-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2022,
       "Valor": 5.7}
    , {"Fecha": "2022-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2022,
       "Valor": 6.8}
    , {"Fecha": "2022-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2022,
       "Valor": 7.3}
    , {"Fecha": "2022-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2022,
       "Valor": 8.9}
    , {"Fecha": "2022-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2022,
       "Valor": 10.5}
    , {"Fecha": "2022-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2022,
       "Valor": 10.8}
    , {"Fecha": "2022-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2022,
       "Valor": 10.2}
    , {"Fecha": "2022-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2022,
       "Valor": 8.7}
    , {"Fecha": "2022-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2022,
       "Valor": 8.3}
    , {"Fecha": "2022-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2022,
       "Valor": 9.8}
    , {"Fecha": "2022-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2022,
       "Valor": 7.6}
    , {"Fecha": "2022-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2022,
       "Valor": 6.1}
    , {"Fecha": "2021-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2021,
       "Valor": 6.5}
    , {"Fecha": "2021-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2021,
       "Valor": 5.5}
    , {"Fecha": "2021-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2021,
       "Valor": 5.4}
    , {"Fecha": "2021-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2021,
       "Valor": 4.0}
    , {"Fecha": "2021-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2021,
       "Valor": 3.3}
    , {"Fecha": "2021-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2021,
       "Valor": 2.9}
    , {"Fecha": "2021-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2021,
       "Valor": 2.7}
    , {"Fecha": "2021-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2021,
       "Valor": 2.7}
    , {"Fecha": "2021-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2021,
       "Valor": 2.2}
    , {"Fecha": "2021-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2021,
       "Valor": 1.3}
    , {"Fecha": "2021-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2021,
       "Valor": 0.0}
    , {"Fecha": "2021-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2021,
       "Valor": 0.5}
    , {"Fecha": "2020-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2020,
       "Valor": -0.5}
    , {"Fecha": "2020-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2020,
       "Valor": -0.8}
    , {"Fecha": "2020-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2020,
       "Valor": -0.8}
    , {"Fecha": "2020-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2020,
       "Valor": -0.4}
    , {"Fecha": "2020-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2020,
       "Valor": -0.5}
    , {"Fecha": "2020-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2020,
       "Valor": -0.6}
    , {"Fecha": "2020-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2020,
       "Valor": -0.3}
    , {"Fecha": "2020-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2020,
       "Valor": -0.9}
    , {"Fecha": "2020-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2020,
       "Valor": -0.7}
    , {"Fecha": "2020-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2020,
       "Valor": 0.0}
    , {"Fecha": "2020-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2020,
       "Valor": 0.7}
    , {"Fecha": "2020-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2020,
       "Valor": 1.1}
    , {"Fecha": "2019-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2019,
       "Valor": 0.8}
    , {"Fecha": "2019-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2019,
       "Valor": 0.4}
    , {"Fecha": "2019-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2019,
       "Valor": 0.1}
    , {"Fecha": "2019-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2019,
       "Valor": 0.1}
    , {"Fecha": "2019-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2019,
       "Valor": 0.3}
    , {"Fecha": "2019-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2019,
       "Valor": 0.5}
    , {"Fecha": "2019-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2019,
       "Valor": 0.4}
    , {"Fecha": "2019-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2019,
       "Valor": 0.8}
    , {"Fecha": "2019-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2019,
       "Valor": 1.5}
    , {"Fecha": "2019-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2019,
       "Valor": 1.3}
    , {"Fecha": "2019-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2019,
       "Valor": 1.1}
    , {"Fecha": "2019-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2019,
       "Valor": 1.0}
    , {"Fecha": "2018-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2018,
       "Valor": 1.2}
    , {"Fecha": "2018-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2018,
       "Valor": 1.7}
    , {"Fecha": "2018-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2018,
       "Valor": 2.3}
    , {"Fecha": "2018-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2018,
       "Valor": 2.3}
    , {"Fecha": "2018-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2018,
       "Valor": 2.2}
    , {"Fecha": "2018-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2018,
       "Valor": 2.2}
    , {"Fecha": "2018-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2018,
       "Valor": 2.3}
    , {"Fecha": "2018-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2018,
       "Valor": 2.1}
    , {"Fecha": "2018-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2018,
       "Valor": 1.1}
    , {"Fecha": "2018-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2018,
       "Valor": 1.2}
    , {"Fecha": "2018-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2018,
       "Valor": 1.1}
    , {"Fecha": "2018-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2018,
       "Valor": 0.6}
    , {"Fecha": "2017-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2017,
       "Valor": 1.1}
    , {"Fecha": "2017-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2017,
       "Valor": 1.7}
    , {"Fecha": "2017-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2017,
       "Valor": 1.6}
    , {"Fecha": "2017-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2017,
       "Valor": 1.8}
    , {"Fecha": "2017-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2017,
       "Valor": 1.6}
    , {"Fecha": "2017-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2017,
       "Valor": 1.5}
    , {"Fecha": "2017-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2017,
       "Valor": 1.5}
    , {"Fecha": "2017-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2017,
       "Valor": 1.9}
    , {"Fecha": "2017-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2017,
       "Valor": 2.6}
    , {"Fecha": "2017-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2017,
       "Valor": 2.3}
    , {"Fecha": "2017-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2017,
       "Valor": 3.0}
    , {"Fecha": "2017-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2017,
       "Valor": 3.0}
    , {"Fecha": "2016-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2016,
       "Valor": 1.6}
    , {"Fecha": "2016-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2016,
       "Valor": 0.7}
    , {"Fecha": "2016-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2016,
       "Valor": 0.7}
    , {"Fecha": "2016-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2016,
       "Valor": 0.2}
    , {"Fecha": "2016-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2016,
       "Valor": -0.1}
    , {"Fecha": "2016-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2016,
       "Valor": -0.6}
    , {"Fecha": "2016-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2016,
       "Valor": -0.8}
    , {"Fecha": "2016-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2016,
       "Valor": -1.0}
    , {"Fecha": "2016-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2016,
       "Valor": -1.1}
    , {"Fecha": "2016-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2016,
       "Valor": -0.8}
    , {"Fecha": "2016-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2016,
       "Valor": -0.8}
    , {"Fecha": "2016-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2016,
       "Valor": -0.3}
    , {"Fecha": "2015-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2015,
       "Valor": 0.0}
    , {"Fecha": "2015-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2015,
       "Valor": -0.3}
    , {"Fecha": "2015-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2015,
       "Valor": -0.7}
    , {"Fecha": "2015-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2015,
       "Valor": -0.9}
    , {"Fecha": "2015-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2015,
       "Valor": -0.4}
    , {"Fecha": "2015-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2015,
       "Valor": 0.1}
    , {"Fecha": "2015-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2015,
       "Valor": 0.1}
    , {"Fecha": "2015-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2015,
       "Valor": -0.2}
    , {"Fecha": "2015-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2015,
       "Valor": -0.6}
    , {"Fecha": "2015-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2015,
       "Valor": -0.7}
    , {"Fecha": "2015-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2015,
       "Valor": -1.1}
    , {"Fecha": "2015-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2015,
       "Valor": -1.3}
    , {"Fecha": "2014-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2014,
       "Valor": -1.0}
    , {"Fecha": "2014-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2014,
       "Valor": -0.4}
    , {"Fecha": "2014-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2014,
       "Valor": -0.1}
    , {"Fecha": "2014-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2014,
       "Valor": -0.2}
    , {"Fecha": "2014-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2014,
       "Valor": -0.5}
    , {"Fecha": "2014-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2014,
       "Valor": -0.3}
    , {"Fecha": "2014-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2014,
       "Valor": 0.1}
    , {"Fecha": "2014-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2014,
       "Valor": 0.2}
    , {"Fecha": "2014-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2014,
       "Valor": 0.4}
    , {"Fecha": "2014-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2014,
       "Valor": -0.1}
    , {"Fecha": "2014-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2014,
       "Valor": 0.0}
    , {"Fecha": "2014-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2014,
       "Valor": 0.2}
    , {"Fecha": "2013-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2013,
       "Valor": 0.3}
    , {"Fecha": "2013-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2013,
       "Valor": 0.2}
    , {"Fecha": "2013-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2013,
       "Valor": -0.1}
    , {"Fecha": "2013-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2013,
       "Valor": 0.3}
    , {"Fecha": "2013-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2013,
       "Valor": 1.5}
    , {"Fecha": "2013-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2013,
       "Valor": 1.8}
    , {"Fecha": "2013-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2013,
       "Valor": 2.1}
    , {"Fecha": "2013-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2013,
       "Valor": 1.7}
    , {"Fecha": "2013-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2013,
       "Valor": 1.4}
    , {"Fecha": "2013-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2013,
       "Valor": 2.4}
    , {"Fecha": "2013-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2013,
       "Valor": 2.8}
    , {"Fecha": "2013-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2013,
       "Valor": 2.7}
    , {"Fecha": "2012-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2012,
       "Valor": 2.9}
    , {"Fecha": "2012-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2012,
       "Valor": 2.9}
    , {"Fecha": "2012-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2012,
       "Valor": 3.5}
    , {"Fecha": "2012-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2012,
       "Valor": 3.4}
    , {"Fecha": "2012-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2012,
       "Valor": 2.7}
    , {"Fecha": "2012-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2012,
       "Valor": 2.2}
    , {"Fecha": "2012-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2012,
       "Valor": 1.9}
    , {"Fecha": "2012-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2012,
       "Valor": 1.9}
    , {"Fecha": "2012-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2012,
       "Valor": 2.1}
    , {"Fecha": "2012-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2012,
       "Valor": 1.9}
    , {"Fecha": "2012-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2012,
       "Valor": 2.0}
    , {"Fecha": "2012-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2012,
       "Valor": 2.0}
    , {"Fecha": "2011-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2011,
       "Valor": 2.4}
    , {"Fecha": "2011-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2011,
       "Valor": 2.9}
    , {"Fecha": "2011-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2011,
       "Valor": 3.0}
    , {"Fecha": "2011-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2011,
       "Valor": 3.1}
    , {"Fecha": "2011-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2011,
       "Valor": 3.0}
    , {"Fecha": "2011-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2011,
       "Valor": 3.1}
    , {"Fecha": "2011-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2011,
       "Valor": 3.2}
    , {"Fecha": "2011-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2011,
       "Valor": 3.5}
    , {"Fecha": "2011-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2011,
       "Valor": 3.8}
    , {"Fecha": "2011-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2011,
       "Valor": 3.6}
    , {"Fecha": "2011-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2011,
       "Valor": 3.6}
    , {"Fecha": "2011-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2011,
       "Valor": 3.3}
    , {"Fecha": "2010-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2010,
       "Valor": 3.0}
    , {"Fecha": "2010-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2010,
       "Valor": 2.3}
    , {"Fecha": "2010-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2010,
       "Valor": 2.3}
    , {"Fecha": "2010-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2010,
       "Valor": 2.1}
    , {"Fecha": "2010-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2010,
       "Valor": 1.8}
    , {"Fecha": "2010-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2010,
       "Valor": 1.9}
    , {"Fecha": "2010-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2010,
       "Valor": 1.5}
    , {"Fecha": "2010-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2010,
       "Valor": 1.8}
    , {"Fecha": "2010-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2010,
       "Valor": 1.5}
    , {"Fecha": "2010-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2010,
       "Valor": 1.4}
    , {"Fecha": "2010-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2010,
       "Valor": 0.8}
    , {"Fecha": "2010-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2010,
       "Valor": 1.0}
    , {"Fecha": "2009-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2009,
       "Valor": 0.8}
    , {"Fecha": "2009-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2009,
       "Valor": 0.3}
    , {"Fecha": "2009-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2009,
       "Valor": -0.7}
    , {"Fecha": "2009-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2009,
       "Valor": -1.0}
    , {"Fecha": "2009-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2009,
       "Valor": -0.8}
    , {"Fecha": "2009-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2009,
       "Valor": -1.4}
    , {"Fecha": "2009-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2009,
       "Valor": -1.0}
    , {"Fecha": "2009-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2009,
       "Valor": -0.9}
    , {"Fecha": "2009-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2009,
       "Valor": -0.2}
    , {"Fecha": "2009-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2009,
       "Valor": -0.1}
    , {"Fecha": "2009-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2009,
       "Valor": 0.7}
    , {"Fecha": "2009-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2009,
       "Valor": 0.8}
    , {"Fecha": "2008-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2008,
       "Valor": 1.4}
    , {"Fecha": "2008-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2008,
       "Valor": 2.4}
    , {"Fecha": "2008-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2008,
       "Valor": 3.6}
    , {"Fecha": "2008-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2008,
       "Valor": 4.5}
    , {"Fecha": "2008-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2008,
       "Valor": 4.9}
    , {"Fecha": "2008-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2008,
       "Valor": 5.3}
    , {"Fecha": "2008-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2008,
       "Valor": 5.0}
    , {"Fecha": "2008-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2008,
       "Valor": 4.6}
    , {"Fecha": "2008-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2008,
       "Valor": 4.2}
    , {"Fecha": "2008-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2008,
       "Valor": 4.5}
    , {"Fecha": "2008-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2008,
       "Valor": 4.4}
    , {"Fecha": "2008-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2008,
       "Valor": 4.3}
    , {"Fecha": "2007-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2007,
       "Valor": 4.2}
    , {"Fecha": "2007-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2007,
       "Valor": 4.1}
    , {"Fecha": "2007-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2007,
       "Valor": 3.6}
    , {"Fecha": "2007-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2007,
       "Valor": 2.7}
    , {"Fecha": "2007-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2007,
       "Valor": 2.2}
    , {"Fecha": "2007-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2007,
       "Valor": 2.2}
    , {"Fecha": "2007-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2007,
       "Valor": 2.4}
    , {"Fecha": "2007-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2007,
       "Valor": 2.3}
    , {"Fecha": "2007-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2007,
       "Valor": 2.4}
    , {"Fecha": "2007-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2007,
       "Valor": 2.5}
    , {"Fecha": "2007-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2007,
       "Valor": 2.4}
    , {"Fecha": "2007-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2007,
       "Valor": 2.4}
    , {"Fecha": "2006-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2006,
       "Valor": 2.7}
    , {"Fecha": "2006-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2006,
       "Valor": 2.6}
    , {"Fecha": "2006-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2006,
       "Valor": 2.5}
    , {"Fecha": "2006-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2006,
       "Valor": 2.9}
    , {"Fecha": "2006-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2006,
       "Valor": 3.7}
    , {"Fecha": "2006-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2006,
       "Valor": 4.0}
    , {"Fecha": "2006-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2006,
       "Valor": 3.9}
    , {"Fecha": "2006-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2006,
       "Valor": 4.0}
    , {"Fecha": "2006-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2006,
       "Valor": 3.9}
    , {"Fecha": "2006-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2006,
       "Valor": 3.9}
    , {"Fecha": "2006-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2006,
       "Valor": 4.0}
    , {"Fecha": "2006-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2006,
       "Valor": 4.2}
    , {"Fecha": "2005-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2005,
       "Valor": 3.7}
    , {"Fecha": "2005-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2005,
       "Valor": 3.4}
    , {"Fecha": "2005-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2005,
       "Valor": 3.5}
    , {"Fecha": "2005-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2005,
       "Valor": 3.7}
    , {"Fecha": "2005-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2005,
       "Valor": 3.3}
    , {"Fecha": "2005-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2005,
       "Valor": 3.3}
    , {"Fecha": "2005-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2005,
       "Valor": 3.1}
    , {"Fecha": "2005-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2005,
       "Valor": 3.1}
    , {"Fecha": "2005-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2005,
       "Valor": 3.5}
    , {"Fecha": "2005-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2005,
       "Valor": 3.4}
    , {"Fecha": "2005-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2005,
       "Valor": 3.3}
    , {"Fecha": "2005-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2005,
       "Valor": 3.1}
    , {"Fecha": "2004-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2004,
       "Valor": 3.2}
    , {"Fecha": "2004-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2004,
       "Valor": 3.5}
    , {"Fecha": "2004-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2004,
       "Valor": 3.6}
    , {"Fecha": "2004-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2004,
       "Valor": 3.2}
    , {"Fecha": "2004-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2004,
       "Valor": 3.3}
    , {"Fecha": "2004-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2004,
       "Valor": 3.4}
    , {"Fecha": "2004-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2004,
       "Valor": 3.5}
    , {"Fecha": "2004-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2004,
       "Valor": 3.4}
    , {"Fecha": "2004-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2004,
       "Valor": 2.7}
    , {"Fecha": "2004-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2004,
       "Valor": 2.1}
    , {"Fecha": "2004-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2004,
       "Valor": 2.1}
    , {"Fecha": "2004-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2004,
       "Valor": 2.3}
    , {"Fecha": "2003-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2003,
       "Valor": 2.6}
    , {"Fecha": "2003-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2003,
       "Valor": 2.8}
    , {"Fecha": "2003-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2003,
       "Valor": 2.6}
    , {"Fecha": "2003-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2003,
       "Valor": 2.9}
    , {"Fecha": "2003-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2003,
       "Valor": 3.0}
    , {"Fecha": "2003-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2003,
       "Valor": 2.8}
    , {"Fecha": "2003-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2003,
       "Valor": 2.7}
    , {"Fecha": "2003-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2003,
       "Valor": 2.7}
    , {"Fecha": "2003-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2003,
       "Valor": 3.1}
    , {"Fecha": "2003-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2003,
       "Valor": 3.7}
    , {"Fecha": "2003-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2003,
       "Valor": 3.8}
    , {"Fecha": "2003-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2003,
       "Valor": 3.7}
    , {"Fecha": "2002-12-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M12", "Anyo": 2002,
       "Valor": 4.0}
    , {"Fecha": "2002-11-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M11", "Anyo": 2002,
       "Valor": 3.9}
    , {"Fecha": "2002-10-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M10", "Anyo": 2002,
       "Valor": 4.0}
    , {"Fecha": "2002-09-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M09", "Anyo": 2002,
       "Valor": 3.5}
    , {"Fecha": "2002-08-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M08", "Anyo": 2002,
       "Valor": 3.6}
    , {"Fecha": "2002-07-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M07", "Anyo": 2002,
       "Valor": 3.4}
    , {"Fecha": "2002-06-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M06", "Anyo": 2002,
       "Valor": 3.4}
    , {"Fecha": "2002-05-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M05", "Anyo": 2002,
       "Valor": 3.6}
    , {"Fecha": "2002-04-01T00:00:00.000+02:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M04", "Anyo": 2002,
       "Valor": 3.6}
    , {"Fecha": "2002-03-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M03", "Anyo": 2002,
       "Valor": 3.1}
    , {"Fecha": "2002-02-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M02", "Anyo": 2002,
       "Valor": 3.1}
    , {"Fecha": "2002-01-01T00:00:00.000+01:00", "T3_TipoDato": "Definitivo", "T3_Periodo": "M01", "Anyo": 2002,
       "Valor": 3.1}]

insertion = ipc_data_2023.insert_many(bulk_data)

for entry in ipc_data_2023.find():
    pprint.pprint(entry)
