//components
import WorkSlider from '../../components/WorkSlider';
import Bulb from '../../components/Bulb';
import Circles from '../../components/Circles';
import Link from 'next/link';

//framer motion
import {motion} from 'framer-motion';
import {fadeIn} from '../../variants';
import {BsArrowRight} from 'react-icons/bs';

const Work = () => {
  return (
    <div className='h-full bg-primary/30 py-36 flex items-center'>
      <Circles/>
      <div className='container mx-auto'>
        <div className='flex flex-col xl:flex-row gap-x-8'>
          {/*text*/}
          <div className='text-center flex xl:w-[30vw] flex-col lg:text-left mb-4 xl:mb-0'>
            <motion.h2 variants={fadeIn('up',0.2)} initial='hidden' animate='show' exit='hidden' className='h2 xl:mt-8'>
              My Work <span className='text-accent'></span>
            </motion.h2>
            <motion.p variants={fadeIn('up',0.2)} initial='hidden' animate='show' exit='hidden' className='mb-4 max-w-[400px] mx-auto lg:mx-0'>
               My projects utilize a wide range of technology, those done at a personal level, for academic purpose and at professional level. All this is done to constantly practise and improve on my skills and knowledge
            </motion.p>
            <Link href={'https://drive.google.com/file/d/1LuD4Xvoh-iC9Gv2Q3kQ7-Oo1ZDPSRsZL/view?usp=sharing'} target="_blank">
              <div className='flex items-center gap-2'>
                <div>My Resume</div>
                <div><BsArrowRight /></div>
              </div>
            </Link>
          </div>
          <motion.div ariants={fadeIn('down',0.6)} initial='hidden' animate='show' exit='hidden' className='w-full xl:max-w-[65%]'>
            <WorkSlider/>
          </motion.div>
        </div>
      </div>
      <Bulb/>
    </div>
  );
};

export default Work;
