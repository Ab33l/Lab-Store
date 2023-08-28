import React, {useState} from 'react';

//icons
import {
  FaHtml5,
  FaCss3,
  FaJs,
  FaReact,
  FaFigma,
  FaAws,
  FaJava,
} from 'react-icons/fa';

import {
  SiNextdotjs,
  SiFramer,
  SiAdobephotoshop,
  SiAdobexd,
  SiFirebase,
} from 'react-icons/si';

import{
  DiAndroid,
  DiPython,
  DiDotnet,
  DiProlog,
} from 'react-icons/di';

//  data
const aboutData = [
  {
    title: 'skills',
    info: [
      {
        title: 'Full Stack Development',
        icons: [
          <FaHtml5 />,
          <FaCss3 />,
          <FaJs />,
          <FaReact />,
          <SiNextdotjs />,
          <SiFramer />,
          <DiDotnet/>,
        ],
      },
      {
        title: 'UI/UX Design',
        icons: [<FaFigma />, <SiAdobexd />, <SiAdobephotoshop />],
      },
      {
        title: 'Mobile App Development',
        icons: [<DiAndroid/>, <SiFirebase/>, <FaJava/>],
      },
      {
        title: 'Machine Learning and Cloud Computing',
        icons: [<DiPython/>, <DiProlog/>, <FaAws/>]
      }
    ],
  },
  {
    title: 'awards',
    info: [
      {
        title: "Absa Bank Kenya PLC, Inter-Bank Games, Checker - Runners Up",
        stage: '2022',
      },
      {
        title: '"My Turn” Annual Antimicrobial Resistance (AMR) Exhibition Event for Kenyan Students using Machine Learning - Finalist',
        stage: '2021',
      },
      {
        title: "Dean's List - Strathmore University",
        stage: 'Academic Year 2016/2017',
      },
    ],
  },
  {
    title: 'experience',
    info: [
      {
        title: 'Graduate Management Trainee - Absa Bank PLC, Kenya',
        stage: '(2022 -)',
      },
      {
        title: 'Software Developer - Comitium, United Kingdom',
        stage: '(2020 - 2023)',
      },
      {
        title: 'Software Engineer - Klevoya, United Kingdom',
        stage: '(2020 - 2020)',
      },
      {
        title: 'PHP Developer - Canvaas Softwares, India',
        stage: '(2019 - 2020)',
      },
      {
        title: 'IT Intern - Meru University of Science and Technology, Kenya',
        stage: '(2019 - 2019)',
      },
    ],
  },
  {
    title: 'Professional Certificates',
    info: [
      {
        title: 'Certified in Cybersecurity with (ISC)2',
        stage: '2023',
      },
      {
        title: 'Amazon Web Services (AWS) Certified Cloud Practitioner with Amazon Web Services',
        stage: '2023',
      },
      {
        title: ' Application Security Specialist with IBM Security AppScan V8.7',
        stage: '2016',
      },
      {
        title: 'Business Intelligence Specialist with Cognos Report Studio V10.2.2',
        stage: '2016',
      },
      {
        title: 'Cisco IT Fundamentals',
        stage: '2016',
      },
    ],
  },
];

//components
import Avatar from '../../components/Avatar';
import Circles from '../../components/Circles';

//framer motion
import {motion} from 'framer-motion';
import {fadeIn} from '../../variants';

//counter
import CountUp from 'react-countup';

const About = () => {
  const [index, setIndex] = useState(0);
  return (
    <div className='h-full bg-primary/30 py-32 text-center xl:text-left'>
      <Circles/>
      {/*avatar image */}
      <motion.div variants={fadeIn('right',0.2)} initial='hidden' animate='show' exit='hidden' className="hidden xl:flex absolute bottom-0 -left-[370px]">
        <Avatar/>
      </motion.div>
      <div className='container mx-auto h-full flex flex-col items-center xl:flex-row gap-x-6'>
        <div className='flex-1 flex flex-col justify-center'>
          <motion.h2 variants={fadeIn('right',0.2)} initial='hidden' animate='show' exit='hidden' className='h2'>About <span className='text-accent'>Me</span></motion.h2>
          <motion.p variants={fadeIn('right',0.4)} initial='hidden' animate='show' exit='hidden' className='max-w-[500px] mx-auto xl:mx-0 mb-6 xl:mb-12 px-2 xl:px-0'>
            A life-long learner always eager to take on new challenges with the aim of coming up with data-informed solutions
          </motion.p>
          {/*counter */}
          <motion.div variants={fadeIn('right',0.6)} initial='hidden' animate='show' exit='hidden' className='hidden md:flex md:max-w-xl xl:max-w-none mx-auto xl:mx-0 mb-8'>
            <div className='flex flex-1 xl:gap-x-6'>
              {/*full stack proficiency*/}
              <div className='relative flex-0 after:w-[1px] after:h-full after:bg-white/10 after:absolute after:top-0 after-right-0'>
                <div className='text-2xl xl:text-4xl font-extrabold text-accent mb-3'>
                  <CountUp start={0} end={87} duration={5}/> %
                </div>
                <div className='text-xs uppercase tracking-[1px] leading-[1.4] max-w-[100px]'>Fullstack proficiency</div>
              </div>
              {/*Programming proficiency*/}
              <div className='relative flex-0 after:w-[1px] after:h-full after:bg-white/10 after:absolute after:top-0 after-right-0'>
                <div className='text-2xl xl:text-4xl font-extrabold text-accent mb-3'>
                  <CountUp start={0} end={88} duration={5}/> %
                </div>
                <div className='text-xs uppercase tracking-[1px] leading-[1.4] max-w-[100px]'>Programming proficiency</div>
              </div>
            </div>
          </motion.div>
        </div>
        {/*info*/}
        <motion.div variants={fadeIn('left',0.4)} initial='hidden' animate='show' exit='hidden' className='flex flex-col w-full xl:max-w-[48%] h-[480px]'>
          <div className='flex gap-x-4 xl:gap-x-8 mx-auto xl:mx-0 mb-4'>
            {aboutData.map((item, itemIndex) =>{
              return(
                <div key={itemIndex} className={`${index === itemIndex && 'text-accent after:w-[100%] after:bg-accent after:transition-all after:duration-300'} cursor-pointer capitalize xl:text-lg relative after:w-8 after:h-[2px] after:bg-white after:absolute after:-bottom-1 after:left-0`} onClick={() => setIndex(itemIndex)}>           
                {item.title}
                </div>
              );
            })}
          </div>
          <div className='py-2 xl:py-6 flex flex-col gap-y-2 xl:gap-y-4 items-center xl:items-start'>
            {aboutData[index].info.map((item, itemIndex) => {
              return(
                <div key={itemIndex} className='flex-1 flex flex-col md:flex-row max-w-max gap-x-2 items-center text-white/60'>
                  {/*title*/}
                  <div className='font-light mb-2 md:mb-0'>{item.title}</div>
                  <div className='hidden md:flex'>-</div>
                  <div>{item.stage}</div>
                  <div className='flex gap-x-4'>
                    {/*icons*/}
                    {item.icons?.map((icon, itemIndex) =>{
                      return <div key={itemIndex} className='text-2xl text-white'>{icon}</div>
                    })}
                  </div>
                </div>
              );
            })}
          </div>
        </motion.div>
      </div>
    </div>
  );
};

export default About;
