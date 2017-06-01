import android.os.Bundle;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

public class TtUuFragment extends Fragment {
    private TtUuViewModel viewModel;
    public static TtUuFragment newInstance() {

        Bundle args = new Bundle();

        TtUuFragment fragment = new TtUuFragment();
        fragment.setArguments(args);
        return fragment;
    }
    @Override
    public View onCreateView(LayoutInflater inflater,  ViewGroup container,  Bundle savedInstanceState) {
        FragmentTtUuBinding binding = FragmentTtUuBinding.inflate(inflater,container,false);
        binding.setViewmodel(viewModel);
        return binding.getRoot();
    }

    public void setViewModel(TtUuViewModel viewModel) {
        this.viewModel = viewModel;
    }
}
