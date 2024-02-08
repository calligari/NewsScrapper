-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Feb 08, 2024 at 08:14 PM
-- Server version: 11.2.2-MariaDB
-- PHP Version: 8.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `NewsScrapper`
--

-- --------------------------------------------------------

--
-- Table structure for table `Websites`
--

CREATE TABLE `Websites` (
  `domain` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `Websites`
--

INSERT INTO `Websites` (`domain`) VALUES
('https://www.elpatagonico.com'),
('https://www.diariocronica.com.ar'),
('https://www.elchubut.com.ar'),
('https://www.adnsur.com.ar'),
('https://elcomodorense.net'),
('https://lapostacomodorense.com.ar'),
('https://www.eldiarioweb.com'),
('https://www.tiemposur.com.ar'),
('https://laopinionaustral.com.ar'),
('https://opisantacruz.com.ar'),
('https://elperiodicoaustral.net'),
('https://vocesyapuntes.com/v6/'),
('https://lavanguardianoticias.com.ar'),
('http://www.eldiariodelfindelmundo.com'),
('https://www.provincia23.com.ar'),
('http://adnrionegro.com.ar'),
('https://www.lmneuquen.com'),
('http://www.noticiasonline.org'),
('https://www.diariamenteneuquen.com.ar'),
('https://www.elextremosur.com'),
('https://www.diariojornada.com.ar'),
('https://www.eldiarionuevodia.com.ar'),
('https://www.minutoneuquen.com'),
('https://fmbahiaengano.com'),
('https://www.rionegro.com.ar'),
('https://www.adnrionegro.com.ar/'),
('http://www.supledesarrollo.com.ar'),
('https://www.mejorinformado.com'),
('https://www.neuquenalinstante.com.ar'),
('https://www.cutralcoalinstante.com'),
('https://rincon.com.ar'),
('https://weblavoz.com.ar'),
('https://www.eldiariodelapampa.com.ar'),
('https://www.vacamuertanews.com'),
('https://www.bariloche2000.com'),
('https://www.diariolapalabra.com.ar'),
('https://www.laarena.com.ar'),
('https://www.lareforma.com.ar'),
('http://periodicolasheras.com.ar'),
('http://tropicalrawson.com'),
('https://radio3cadenapatagonia.com.ar'),
('https://lu17.com'),
('https://www.red43.com.ar'),
('https://www.ambito.com'),
('https://www.cronista.com'),
('https://www.pagina12.com.ar'),
('https://www.lanacion.com.ar'),
('https://www.clarin.com'),
('https://www.infobae.com/?noredirect'),
('https://www.perfil.com'),
('https://cholilaonline.ar'),
('https://www.lateclapatagonia.com.ar/actualidad'),
('http://www.argentarnoticias.com.ar'),
('https://vaconfirma.com.ar'),
('https://centenariodigital.com'),
('https://www.lmcipolletti.com'),
('https://elintra.com.ar'),
('https://www.eltribuno.com/salta'),
('https://www.quepasasalta.com.ar'),
('https://informatesalta.com.ar'),
('https://www.lagaceta.com.ar/tags/638/salta'),
('https://www.nuevodiariodesalta.com.ar'),
('http://www.fm899.com.ar'),
('https://cuartopodersalta.com.ar'),
('http://noticias.iruya.com/a/'),
('http://www.diariopuntouno.com.ar/dp1_a/index.php'),
('https://salta21.com'),
('https://www.lahoradesalta.com.ar'),
('https://laprensadesantacruz.info'),
('https://www.mediaticadigital.com.ar'),
('https://fuego24.com'),
('fmalbatartagal'),
('https://www.letrap.com.ar/region/patagonia'),
('https://opsur.org.ar'),
('https://noticiasnqn.com.ar'),
('https://fmalba.com.ar'),
('https://enernews.com'),
('https://miningpress.com'),
('https://oncediario.com.ar'),
('https://www.elinversorenergetico.com'),
('https://www.energiaspatagonicas.com'),
('https://www.petrolnews.net'),
('https://www.revistapetroquimica.com'),
('https://noalamina.org'),
('http://depetroleo.com'),
('https://econojournal.com.ar'),
('https://suractual.com.ar'),
('https://radiodelmar.net'),
('https://inneuquen.info'),
('https://www.tunoticia.com.ar'),
('https://realidadeconomica.com.ar'),
('https://explicitoonline.com'),
('https://patagoniashale.com.ar'),
('https://tartagalaldia.com.ar'),
('https://www.sur54.com'),
('https://www.surenio.com.ar'),
('https://www.actualidadtdf.com.ar'),
('https://radatillynoticias.com'),
('https://www.elcaletense.net'),
('https://canalnueve.tv/seccion/actualidad'),
('https://www.milpatagonias.com'),
('https://www.eldigitalneuquen.com.ar'),
('https://www.losandes.com.ar'),
('https://www.mdzol.com'),
('https://www.diariouno.com.ar'),
('https://universidadcalf.com'),
('https://mase.lmneuquen.com'),
('https://www.santacruzenelmundo.com'),
('https://catriel25noticias.com'),
('http://vivocomodoro.com.ar'),
('-'),
('https://rtn.com.ar'),
('https://noticiaslasheras.com.ar'),
('https://www.znnoticias.com'),
('https://www.catrielonline.com.ar'),
('https://diario10.com.ar'),
('https://www.diarioneuquino.com.ar'),
('https://vientosurnoticias.com.ar'),
('https://www.nqn3.com'),
('https://diariotextual.com/inicio/'),
('https://www.noticias7.com'),
('https://www.elancasti.com.ar'),
('https://www.elesquiu.com'),
('https://andalgalaadiario.blogspot.com'),
('https://www.catamarcactual.com.ar'),
('https://www.eldiariodecatamarca.com'),
('https://agenciatierraviva.com.ar'),
('https://www.mejorenergia.com.ar'),
('https://www.eldiario.com.ar'),
('https://www.elheraldo.com.ar/'),
('https://www.unoentrerios.com.ar'),
('https://entreriosahora.com'),
('https://entreriosya.com.ar'),
('https://www.elentrerios.com'),
('https://entremediosweb.com'),
('https://ahora.com.ar'),
('https://www.miradorprovincial.com'),
('https://www.eldiaonline.com'),
('https://www.diarioelargentino.com.ar'),
('https://maximaonline.com.ar'),
('https://r2820.com'),
('https://www.ellitoral.com.ar'),
('https://www.corrienteshoy.com'),
('https://www.radiodos.com.ar'),
('https://www.radiosudamericana.com'),
('https://www.diarioepoca.com'),
('https://www.diarioellibertador.com.ar'),
('https://www.nortecorrientes.com'),
('https://www.republicadecorrientes.com'),
('https://www.lt7noticias.com'),
('https://energia.news'),
('https://lu19.com.ar'),
('https://infomix.com.ar/'),
('http://elfaropsj.com/index.php/category/regionales/'),
('https://www.telam.com.ar/'),
('https://truncadoinforma.com'),
('https://www.labrujula24.com/'),
('https://www.canalsiete.com.ar/'),
('https://www.lanueva.com/'),
('https://frenteacano.com.ar/');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
