//next image
import Image from 'next/image';

const Avatar = () => {
  return(
    <div className='hidden xl:flex xl:max-w-none'>
      <Image src={'/avatar1.png'} width={666} height={375} alt='' className='translate-z-0 w-full h-full'/>
    </div>
  );
};

export default Avatar;
