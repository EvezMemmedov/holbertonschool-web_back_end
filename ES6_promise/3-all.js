import { uploadPhoto, createUser } from './utils.js';
export default function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      console.log(`${photo.body} ${user.firstName} {user.lastName}`);
    })
    .catch(() => {
      consolo.log('Signup system offline');
    });
}