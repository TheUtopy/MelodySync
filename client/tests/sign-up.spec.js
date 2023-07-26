import { shallowMount } from '@vue/test-utils';
import SignUp from '../pages/sign-up.vue';

describe('SignUp', () => {
    it('displays an error message if username field is empty', async () => {
        const wrapper = shallowMount(SignUp);
        wrapper.find('[data-test="submit-form"]').trigger('submit');
        await wrapper.vm.$nextTick();
        expect(wrapper.text()).toContain('Username is required');
    });
});