//links
import Link from 'next/link';

//icons
import {RiGithubLine, RiLinkedinLine} from 'react-icons/ri';
import {BsGoogle} from 'react-icons/bs';

const Socials = () => {
  return (
    <div className='flex items-center gap-x-5 text-lg'>
      <Link href={'https://github.com/Ab33l'} target="_blank" className='hover:text-accent transition-all duration-300'>
        <RiGithubLine/>
      </Link>
      <Link href={'https://www.linkedin.com/in/abell-wandili-2b27a3177'} target="_blank" className='hover:text-accent transition-all duration-300'>
        <RiLinkedinLine/>
      </Link>
      <Link href={`mailto:abellwandili@gmail.com`} target="_blank" className='hover:text-accent transition-all duration-300'>
        <BsGoogle/>
      </Link>
    </div>
  );
};

export default Socials;
