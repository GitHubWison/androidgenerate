import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class TttPpkFragment extends Fragment {
    private TttPpkViewModel viewModel;
    public static TttPpkFragment newInstance() {

        Bundle args = new Bundle();

        TttPpkFragment fragment = new TttPpkFragment();
        fragment.setArguments(args);
        return fragment;
    }
    @Override
    public View onCreateView(LayoutInflater inflater,  ViewGroup container,  Bundle savedInstanceState) {
        FragmentTttPpkBinding binding = FragmentTttPpkBinding.inflate(inflater,container,false);
        binding.setViewmodel(viewModel);
        return binding.getRoot();
    }

    public void setViewModel(TttPpkViewModel viewModel) {
        this.viewModel = viewModel;
    }
}
