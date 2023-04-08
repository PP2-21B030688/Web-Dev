export interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  rating: number;
  link: string;
  image: string;
}

export const products = [
  {
    id: 1,
    name: 'Samsung Galaxy A23',
    price: 104575,
    description: 'A black phone, 128Gb, LED sensored screen',
    rating: 4.1,
    link: "https://kaspi.kz/shop/p/samsung-galaxy-a23-6-gb-128-gb-chernyi-104348541/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hb5/ha6/49792685244446/smartfon-samsung-galaxy-a23-sm-a235fzkkskz-128gb-black-104348541-1.jpg",
  },
  {
    id: 2,
    name: 'Apple iPhone 11',
    price: 292759,
    description: 'A great phone, 128Gb, stylized SlimBox model',
    rating: 5.0,
    link: "https://kaspi.kz/shop/p/apple-iphone-11-128gb-slim-box-chernyi-100692388/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h17/h14/31489167425566/apple-iphone-11-128gb-slim-box-cernyj-100692388-1-Container.jpg",
  },
  {
    id: 3,
    name: 'ARG ZY-8001W',
    price: 6490,
    description: 'Silver electric teapot, stainless steel',
    rating: 4.0,
    link: "https://kaspi.kz/shop/p/arg-zy-8001w-serebristyi-101378035/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h21/hf8/49988638244894/arg-zy-8001w-serebristyj-101378035-1-Container.jpg",
  },
  {
    id: 4,
    name: 'Keyboard X-Game XK-200UB',
    price: 2824,
    description: 'Shiny colorful keyboards to reach Faceit LVL10',
    rating: 5.0,
    link: "https://kaspi.kz/shop/p/x-game-xk-200ub-chernyi-9200601/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/ha0/h75/31943918518302/x-game-xk-200ub-black-9200601-1-Container.jpg",
  },
  {
    id: 5,
    name: 'Phonecase Ala case для iPhone 11',
    price: 280,
    description: 'Phonecase for iPhone11, let it be safe!',
    rating: 4.0,
    link: "https://kaspi.kz/shop/p/ala-case-dlja-iphone-11-prozrachnyi-103661424/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hc2/h42/48677606293534/ala-case-dla-iphone-11-prozracnyj-103661424-1.jpg",
  },
  {
    id: 6,
    name: 'Graphic tablet Wacom One Medium CTL-672',
    price: 38000,
    description: 'Must-have tablet for drawing, sculpting, showing off',
    rating: 4.8,
    link: "https://kaspi.kz/shop/p/wacom-one-medium-ctl-672-18500036/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/had/h83/31703280255006/wacom-one-medium-ctl-672-black-red-18500036-1-Container.jpg",
  },
  {
    id: 7,
    name: 'Microphone Handel K11',
    price: 6898,
    description: 'People should hear your beautiful voice with the help of this device',
    rating: 4.2,
    link: "https://kaspi.kz/shop/p/handel-k11-106313925/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h18/h1e/62189525499934/handel-k11-2-sht-106313925-1.jpg",
  },
  {
    id: 8,
    name: 'Toaster CENTEK СТ-1432 черный',
    price: 11069,
    description: 'Crispy toasts await for you',
    rating: 3.7,
    link: "https://kaspi.kz/shop/p/centek-st-1432-chernyi-100295343/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h70/hf3/32725893414942/centek-st-1432-cernyj-100295343-1-Container.jpg",
  },
  {
    id: 9,
    name: 'Web-camera A4Tech PK-910H',
    price: 10600,
    description: 'Perfect choice for your ZOOM classes',
    rating: 2.0,
    link: "https://kaspi.kz/shop/p/a4tech-pk-910h-9500054/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/hb5/h2f/31628713820190/a4tech-pk-910h-black-9500054-1-Container.jpg",
  },
  {
    id: 10,
    name: 'Overlock Janome Samurai 888',
    price: 162000,
    description: 'New dress? T-shirt? Pants? You choose',
    rating: 4.9,
    link: "https://kaspi.kz/shop/p/overlok-janome-samurai-888-belyi-9400106/?c=750000000#!/item",
    image: "https://resources.cdn-kaspi.kz/shop/medias/sys_master/images/images/h4f/h40/32033463336990/janome-samurai-888-white-9400106-1.jpg",
  },
];
