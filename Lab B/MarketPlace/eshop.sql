-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 17, 2023 at 08:12 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.0.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `eshop`
--

-- --------------------------------------------------------

--
-- Table structure for table `category`
--

CREATE TABLE `category` (
  `Categoryid` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Parent` int(11) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `category`
--

INSERT INTO `category` (`Categoryid`, `Name`, `Parent`) VALUES
(1, 'Electronics', 0),
(2, 'Health & Beauty', 0),
(3, 'Home & Living', 0),
(4, 'Travel & Accommodation', 0),
(8, 'Household and Kitchen Appliances', 1),
(9, 'Spa services', 2),
(10, 'Hospital ', 2),
(11, 'Medical services', 2),
(12, 'Medical evacuation services', 2),
(13, 'Golf Club Membership', 2),
(14, 'Office Furniture', 3),
(15, 'Home Furniture', 3),
(16, 'Batteries and solar products', 3),
(17, 'House cleaning services', 3),
(18, 'Furniture', 3),
(19, 'Kitchen Appliances', 3),
(20, 'Laundry Services', 3),
(21, 'Building Materials', 3),
(22, 'Domestic and international flights', 4),
(24, 'Accommodation ', 4),
(25, 'Conservertory ', 4);

-- --------------------------------------------------------

--
-- Table structure for table `featured`
--

CREATE TABLE `featured` (
  `id` int(11) NOT NULL,
  `featured` varchar(50) NOT NULL,
  `createdAt` datetime NOT NULL DEFAULT current_timestamp(),
  `updatedAt` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `featured`
--

INSERT INTO `featured` (`id`, `featured`, `createdAt`, `updatedAt`) VALUES
(1, 'Top 8', '2023-07-21 15:56:52', '2023-07-21 15:56:52'),
(2, 'Latest Product', '2023-07-21 15:56:52', '2023-07-21 15:56:52'),
(3, 'Not Featured', '2023-07-21 17:04:32', '2023-07-21 17:04:32'),
(4, 'Biggest Deals', '2023-07-21 17:10:09', '2023-07-21 17:10:09');

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `Productid` int(11) NOT NULL,
  `Category` int(11) DEFAULT NULL,
  `Name` varchar(50) DEFAULT NULL,
  `image` varchar(250) DEFAULT NULL,
  `date_added` datetime NOT NULL DEFAULT current_timestamp(),
  `Discount` int(11) DEFAULT NULL,
  `featured_id` int(11) DEFAULT NULL,
  `officialSite` varchar(255) NOT NULL,
  `productDescription` text NOT NULL,
  `validity` varchar(255) NOT NULL,
  `status_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`Productid`, `Category`, `Name`, `image`, `date_added`, `Discount`, `featured_id`, `officialSite`, `productDescription`, `validity`, `status_id`) VALUES
(1, 8, 'Housewife\'s Paradise', 'https://airduka.com/storage/company_avatars/6502/house-wifes-paradise-1646188194.jpg', '2017-11-04 16:00:00', 10, 1, 'https://housewifesparadise.com/', 'On all Refrigerators, washing machines and free standing cookers - 7.5% reduced from the price tag on display at the shop.\r\n\r\nFree delivery and installation on large items within 15 kilometers from Nairobi CBD; for extra mileage or distance upto 25 kilometers from the CBD, a FLAT FEE OF Ksh. 1,000.00 only\r\n\r\nOn Television sets ABSA very attractive offer prices\r\n\r\nOn all small domestic appliances eg Blenders, Juicers, Toasters, etc - special discount of 10%', '30th June 2023', 1),
(2, 9, 'Spa by Xenaxia', 'https://media.licdn.com/dms/image/C560BAQGK8zI4WtuyuQ/company-logo_200_200/0/1645436903394?e=2147483647&v=beta&t=-3AGRar42tjiJ6Xo4o6h-KGK54v54aW280b_oIP9Fig', '2017-11-04 16:01:00', 10, 1, 'https://spabyxenaxia.com/', '10% off spa services - Norfolk, Wadi Degla, Movenpick', '31st October 2023', 1),
(3, 10, 'Meridian Group ', 'https://media.licdn.com/dms/image/C4D0BAQHVihsmi6YTOQ/company-logo_200_200/0/1632137672277?e=2147483647&v=beta&t=nx5ii84Pi0pdt8QbIdTTRoGMXQV6lGAgyU_CFTKBXA4', '2017-11-04 16:02:00', 10, 1, 'https://mhg.co.ke/', '7.5% discount on consultation, laboratory, radiology (ultra sound, x-ray, drugs)\r\n\r\n10% discount on CT scans\r\n\r\n10% discount on vaccination\r\n\r\n10% off wellness checkup\r\n\r\n5% off inpatient visits', '31st December 2023', 1),
(4, 11, 'Byon8', 'https://media.licdn.com/dms/image/C4E0BAQGJi7Mg9SCKdg/company-logo_200_200/0/1594859668900?e=2147483647&v=beta&t=uqYmEdRIsnAWOvcA3ACXS2_rC8_V4dBFvWCa8JbkHz0', '2017-11-04 16:03:00', 10, 1, 'https://www.byon8.com/', '1. Partnership discount of 10% transferred to all Absa Customers\r\n\r\n2. Quarterly payments attracts an additional 5% discount on annual fees\r\n\r\n3. Semi-annual payments attracts an additional 7.5% discount on annual fees\r\n\r\n4. Annual payment discount attracts an additional 10% discount on annual fees', '31st December 2023', 1),
(5, 12, 'Amref', 'https://media.licdn.com/dms/image/C4D0BAQGapTcnmhEQRA/company-logo_200_200/0/1530170593676?e=2147483647&v=beta&t=Jtq8-fyzY9lFJruLaYQ2n-SK009-AJdnfWie7NbUMd0', '2017-11-04 16:05:00', 0, 1, 'https://amref.org/kenya/', 'No Product Description provided', 'No validity period present', 1),
(6, 13, 'Vetlab Golf', 'No official logo present', '2023-07-20 20:51:35', 0, 3, 'No official website present', 'No Product Description Provided', 'No validity period present', 1),
(7, 14, 'Burotime', 'https://media.licdn.com/dms/image/D4D0BAQE9SuhKTtBoDA/company-logo_200_200/0/1680256354271?e=2147483647&v=beta&t=MmeUjeTCnSYlm2qneH7cxpDmYAqpiTI209q-oaqCJck', '2017-11-04 16:07:00', 10, 1, 'https://burotime.co.ke/', '10% off', '10th April 2023', 1),
(8, 15, 'Istikbal Furniture', 'https://media.licdn.com/dms/image/C560BAQGBgIvxXg8qYw/company-logo_200_200/0/1584355334076?e=2147483647&v=beta&t=nLpMOm6CQUFdIc8-yqB6IzFySW2noXU3sGbVEVwWBzE', '2017-11-04 16:08:00', 10, 1, 'https://www.istikbalkenya.com/', '10% off', '10th April 2023', 1),
(9, 16, 'Chloride Exide', 'https://media.licdn.com/dms/image/C4D0BAQGc5wSUmHpc5Q/company-logo_200_200/0/1641977803759?e=2147483647&v=beta&t=ZPoEM1H6vqX-CMBN8Hd2r8c4UCWPNUx5DxZwRwBaJyY', '2017-11-04 16:09:00', 31, 1, 'https://chlorideexide.com/contact-us/', '31% off locally manufactured Chloride batteries\r\n\r\n22% off imported Chloride batteries\r\n\r\n20% off solar products', '26th June 2023', 1),
(10, 17, 'Sweepsouth', 'https://media.licdn.com/dms/image/C560BAQFpiF2lrfGWZA/company-logo_200_200/0/1649330889952?e=2147483647&v=beta&t=zY21rqby5zkgO94EadpGwC-LhFgnZ2Jy6PxXopEC0b4', '2017-11-04 16:10:00', 0, 2, 'https://ke.sweepsouth.com/', 'Kes 650 off every house cleaning service\r\n\r\n**Nairobi Only**', '31st October 2023', 1),
(11, 18, 'Dogtas Furniture', 'https://media.licdn.com/dms/image/C4D0BAQG_pIyI2dBzcg/company-logo_200_200/0/1519904136299?e=2147483647&v=beta&t=AeuqBjOdxLEDpWqxlpdc1w8ZOJRD0ISSNUcOb4ECgQU', '2017-11-04 16:10:04', 10, 2, 'https://dogtas.co.ke/', '20% off ', '31st April 2023', 1),
(12, 18, 'Victoria Furniture', 'https://media.licdn.com/dms/image/C4D0BAQFYtIVGmE7vfw/company-logo_200_200/0/1519893940756?e=2147483647&v=beta&t=BlIQb_7YuFBs9MjDIJSrlMmsOpdMm6VqBX3NkB3_kJM', '2017-11-04 16:11:00', 9, 2, 'https://www.victoriafurnitures.com/', '5% discount. T&Cs apply - not valid for mattresses, carpets, accessories and any products already on offer.\r\n ', '30th June 2023', 1),
(13, 19, 'Rossetti', 'https://www.rossetticasalinghi.com/wp-content/uploads/2020/07/INVOICE-logo-1.png', '2017-11-04 16:12:00', 0, 3, 'https://www.rossetticasalinghi.com/ke/', 'Spend Kes 10,000 or more and get a Rosetti kitchen knives set', 'While stocks last', 1),
(14, 20, 'Whiterose Drycleaners', 'https://www.iko.co.ke/pictures/img_1417706213310524515.png', '2017-11-04 16:13:00', 10, 3, 'https://www.whiterose.co.ke/', '10% discount', '14th May 2024', 1),
(15, 21, 'Ideal Ceramics', 'https://media.licdn.com/dms/image/C5603AQHrRVdUsIj8CA/profile-displayphoto-shrink_800_800/0/1542281272818?e=2147483647&v=beta&t=bY_RH6fNv0uP9IX7z4smZdaJttTo6uSJO8gsGP0qpX8', '2017-11-04 16:14:00', 15, 3, 'https://www.idealceramics.com/', '15% discount on all products', '31st December 2023', 1),
(16, 22, 'KQ', 'https://media.licdn.com/dms/image/C4D0BAQG55jE1FesTyw/company-logo_200_200/0/1519913468329?e=2147483647&v=beta&t=rAKE_fDKrVFPMDPamKrWeD3NwxiKChMKyUfwgCmatKk', '2017-11-04 16:15:00', 10, 2, 'https://www.kenya-airways.com/za/en/', '10% off net fare', '15th June 2023', 1),
(17, 24, 'The Reef Hotel, Mombasa', 'https://media.licdn.com/dms/image/D5603AQGzDcMT-1Ptsg/profile-displayphoto-shrink_800_800/0/1682670429299?e=2147483647&v=beta&t=Q-glnl6Y7OXsUyl0AS9nGs9alUyRnacCPwuNMxJlLGQ', '2017-11-04 16:16:00', 10, 3, 'https://reefhotelkenya.com/', 'EASTER PERIOD OFFER – VALID 7TH APRIL – 10TH APRIL\r\n\r\nSingle room – ksh 14,000 per room per night on All-inclusive basis \r\n\r\nDouble /twin room – ksh 18,000 per room per night on All-inclusive basis\r\nChild sharing in a double room with two adults – ksh 4500 per child per night\r\n 2 kids in own room – ksh 14,000 per room per night on All-inclusive basis\r\n \r\nAll inclusive : Breakfast, lunch and dinner plus a selection of alcoholic and non-alcoholic drinks inc snacks \r\n\r\n10% discount on the above rates ', '10th April 2023', 1),
(18, 25, 'Ol Pejeta Conservancy', 'https://www.olpejetaconservancy.org/images/decoration/olpejeta-escapes.png', '2017-11-04 16:18:00', 10, 4, 'https://www.olpejetaconservancy.org/', '10% discount for conservation experiences, accommodation and restaurant ', '22nd October 2023', 1),
(19, 13, 'Organic Flavorcrest Peaches', 'https://cdn.shopify.com/s/files/1/0336/7167/5948/products/image-of-organic-flavorcrest-peaches-organics-28658697863212_600x600.jpg?v=1627993298', '2017-11-04 16:19:00', 12, 1, '', '', '', 1),
(20, 14, 'Star Apples', 'https://cdn.shopify.com/s/files/1/0336/7167/5948/products/image-of-star-apples-fruit-33020090286124_600x600.jpg?v=1674510775', '2017-11-04 16:20:00', 11, 0, '', '', '', 1),
(21, 15, 'D\'Anjou Pears', 'https://cdn.shopify.com/s/files/1/0336/7167/5948/products/image-of-d-anjou-pears-fruit-14764270354476_400x400.jpg?v=1616886121', '2017-11-04 16:21:00', 14, 1, '', '', '', 1),
(22, 16, 'Blood Oranges', 'https://cdn.shopify.com/s/files/1/0336/7167/5948/products/image-of-blood-oranges-fruit-28657870143532_600x600.jpg?v=1628015991', '2017-11-04 16:22:00', 6, 1, '', '', '', 1),
(23, 17, 'Kieffer Limes', 'https://cdn.shopify.com/s/files/1/0336/7167/5948/products/image-of-kieffer-limes-fruit-14764176965676_400x400.jpg?v=1625159099', '2017-11-04 16:23:00', 11, 1, '', '', '', 1),
(24, 18, 'Waterloupes', 'https://cdn.shopify.com/s/files/1/0336/7167/5948/products/image-of-waterloupe-fruit-30681856049196_600x600.jpg?v=1656015968', '2017-11-04 16:24:00', 9, 0, '', '', '', 1),
(25, 19, 'Kiwano Horned Melons', 'https://cdn.shopify.com/s/files/1/0336/7167/5948/products/image-of-kiwano-horned-melon-fruit-14764461883436_600x600.jpg?v=1616872562', '2017-11-04 16:24:00', 33, 0, '', '', '', 1),
(26, 20, 'Manzano Bananas', 'https://cdn.shopify.com/s/files/1/0336/7167/5948/products/image-of-manzano-bananas-fruit-14764176244780_400x400.jpg?v=1625603425', '2017-11-04 16:25:00', 40, 0, '', '', '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `staff`
--

CREATE TABLE `staff` (
  `staffId` int(11) NOT NULL,
  `abNumber` varchar(50) NOT NULL,
  `phoneNumber` varchar(100) NOT NULL,
  `email_address` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staff`
--

INSERT INTO `staff` (`staffId`, `abNumber`, `phoneNumber`, `email_address`, `password`, `createdAt`) VALUES
(1, 'ABZ429G', '+254738292855', 'super.admin@absa.africa', 'e7e52d25748fe645402a2777684f65140b8eeb4ec1ab85cb9f2fff0655daec19', '2023-07-30 23:39:45');

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  `createdAt` datetime NOT NULL DEFAULT current_timestamp(),
  `updatedAt` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`id`, `status`, `createdAt`, `updatedAt`) VALUES
(1, 'Active', '2023-07-20 15:51:41', '2023-07-20 15:51:41'),
(2, 'Deactivated', '2023-07-20 15:51:41', '2023-07-20 15:51:41');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `category`
--
ALTER TABLE `category`
  ADD PRIMARY KEY (`Categoryid`);

--
-- Indexes for table `featured`
--
ALTER TABLE `featured`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`Productid`);

--
-- Indexes for table `staff`
--
ALTER TABLE `staff`
  ADD PRIMARY KEY (`staffId`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `category`
--
ALTER TABLE `category`
  MODIFY `Categoryid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `featured`
--
ALTER TABLE `featured`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `Productid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `staff`
--
ALTER TABLE `staff`
  MODIFY `staffId` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
